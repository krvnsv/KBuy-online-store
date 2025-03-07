from store.models import Collection, Product
from django.contrib.auth.models import User
from rest_framework import status
import pytest
from model_bakery import baker

from store.tests.conftest import authenticate

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_return_401(self, create_collection):
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_return_403(self, authenticate, create_collection):
        authenticate()

        response = create_collection({ 'title': 'a'})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_return_400(self, api_client, create_collection):
        authenticate(is_staff=True)
        response = create_collection({ 'title': ''})
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None


    def test_if_data_is_valid_return_201(self, api_client, create_collection):
        authenticate(is_staff=True)
        
        response = create_collection({ 'title': 'a'})
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    
# @pytest.mark.django_db
# class TestRetrieveCollection:
#     def test_if_collection_exists_return_200(self, api_client):
#         # Arrange
#         collection = baker.make(Collection)

#         response = api_client.get(f'/store/collections{collection.id}')

#         assert response.status_code == status.HTTP_200_OK
#         assert response.data == {
#             'id': collection.id,
#             'title': collection.title
#         }