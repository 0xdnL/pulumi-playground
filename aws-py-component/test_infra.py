import unittest
import pulumi

class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, type_, name, inputs, provider, id_):
        return [name + '_id', inputs]
    def call(self, token, args, provider):
        return {}

pulumi.runtime.set_mocks(MyMocks())


import infra

class TestingWithMocks(unittest.TestCase):
    # Test if the service has tags and a managedByy tag
    @pulumi.runtime.test
    def test_bucket_tags(self):

        def check_tags(args):
            urn, tags = args
            self.assertIsNotNone(tags, f'bucket {urn} must have tags')
            self.assertIn('managedBy', tags, 'bucket {urn} must have a managedBy tag')

        return pulumi.Output.all(infra.someBucket.urn, infra.someBucket.tags).apply(check_tags)
