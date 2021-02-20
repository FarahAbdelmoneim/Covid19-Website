
try:
    from COVID_19_Monitor import app
    import unittest
except Exception as e:
    print("Missing modules {}",format(e))
    
    
class test_form(unittest.TestCase):
    
    def test_response(self):
#        self.assertEqual(resp.status,'200 OK')
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

# testing the type of content returned 
    def test_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')
        
# checking for data returned    
    def test_message(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'cases' in response.data)
        
class TestConfig(unittest.TestCase):
    def test_config__loading(self):
        self.assertFalse (app.config['DEBUG']) #To test the debug option
        
    def test_welcome_route_works_as_expected(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertIn(b'COVID-19 Monitor', response.data) # Ensure that welcome page loads
        
    def testing_cases_cum(self):
        tester = app.test_client(self)
#        response = tester.get("/")
        self.assertEqual (tester.get("/?country=egypt&status=cases_cum").status,'200 OK')
        
    def testing_deaths_cum(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=italy&status=deaths_cum").status,'200 OK')
        
    def testing_daily_cases(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=france&status=cases").status,'200 OK')
        
    def testing_daily_deaths(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=germany&status=deaths").status,'200 OK')
        
    def testing_finding_R0(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=USA&status=Find R0").status,'200 OK')
    
    def testing_CasesCum(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=spain&status=cases_cum").status,'200 OK')
        
    def testing_DeathsCum(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=Russia&status=deaths_cum").status,'200 OK')
        
    def testing_DailyCases(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=ksa&status=cases").status,'200 OK')
        
    def testing_DailyDeaths(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=palastine&status=deaths").status,'200 OK')
        
    def testing_FindingR0(self):
        tester = app.test_client(self)
        self.assertEqual (tester.get("/?country=UAE&status=Find R0").status,'200 OK')
        
if __name__=='__main__':
    unittest.main()