from django.test import TestCase
from django.urls import reverse

class ApisTestCase(TestCase):
    
    def test_recommend_words(self):
        response_json = self.client.get(reverse('mytube-api-recommend-words')).json()
        self.assertTrue('recommend_words' in response_json)
        self.assertTrue(len(response_json['recommend_words']) > 0)

    def test_error_response(self):
        response = self.client.get(reverse('mytube-api-recommend-words')+'?error_status=500')
        self.assertEqual(response.status_code, 500)
        response = self.client.get(reverse('mytube-api-recommend-words')+'?error_status=403')
        self.assertEqual(response.status_code, 403)

    def test_search(self):
        response_json = self.client.get('%s?q=%s' % (reverse('mytube-api-search'), '골프')).json()
        self.assertTrue('search_results' in response_json)
        self.assertTrue(len(response_json['search_results']) > 0)
        response_json = self.client.get('%s?q=%s&max_size=%d' % (reverse('mytube-api-search'), '탁구', 5)).json()
        self.assertTrue('search_results' in response_json)
        self.assertEqual(len(response_json['search_results']), 5)
        response_json = self.client.get('%s?q=%s&max_size=%d' % (reverse('mytube-api-search'), '농구', 0)).json()
        self.assertTrue('search_results' in response_json)
        self.assertEqual(len(response_json['search_results']), 0)
