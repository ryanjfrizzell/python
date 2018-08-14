# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.apiextensions_v1beta1_api import ApiextensionsV1beta1Api


class TestApiextensionsV1beta1Api(unittest.TestCase):
    """ ApiextensionsV1beta1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.apiextensions_v1beta1_api.ApiextensionsV1beta1Api()

    def tearDown(self):
        pass

    def test_create_custom_resource_definition(self):
        """
        Test case for create_custom_resource_definition

        
        """
        pass

    def test_delete_collection_custom_resource_definition(self):
        """
        Test case for delete_collection_custom_resource_definition

        
        """
        pass

    def test_delete_custom_resource_definition(self):
        """
        Test case for delete_custom_resource_definition

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_custom_resource_definition(self):
        """
        Test case for list_custom_resource_definition

        
        """
        pass

    def test_patch_custom_resource_definition(self):
        """
        Test case for patch_custom_resource_definition

        
        """
        pass

    def test_patch_custom_resource_definition_status(self):
        """
        Test case for patch_custom_resource_definition_status

        
        """
        pass

    def test_read_custom_resource_definition(self):
        """
        Test case for read_custom_resource_definition

        
        """
        pass

    def test_read_custom_resource_definition_status(self):
        """
        Test case for read_custom_resource_definition_status

        
        """
        pass

    def test_replace_custom_resource_definition(self):
        """
        Test case for replace_custom_resource_definition

        
        """
        pass

    def test_replace_custom_resource_definition_status(self):
        """
        Test case for replace_custom_resource_definition_status

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
