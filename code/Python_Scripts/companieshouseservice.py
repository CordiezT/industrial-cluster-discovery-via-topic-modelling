##CompaniesHouseService.py##

import requests
import json
import datetime
import time

class CompaniesHouseService:
    """A wrapper around the companies house API.
    
    Attributes:
        search_url (str): Base url for Companies House search query.
        company_url (str): Base url for Companies House company query.
        
    """
    search_url = "https://api.companieshouse.gov.uk/search/companies?q={}"
    company_url = "https://api.companieshouse.gov.uk/company/{}"
    
    def __init__(self, key, time_between_requests=0.5):
        """
        Args:
            key (str): The API key issued in the Companies House API 
                applications.
            time_between_requests (float): Time in seconds between requests to 
                the API to prevent spam. Default is 0.5 to prevent calls 
                exceeding the 600 per 5 minutes limit.
            
        """
        self.key = key
        self.time_between_requests = time_between_requests
        
        #: datetime: Timestamp instantiated as NoneType 
        self.last_request_timestamp = None
    
    def _query_ch_api(self, url, query):
        """Sends a request to the Companies House API.
        
        Args:
            url (str): The specific url to be queried depending on the type
                of request (search, profile etc.).
            query (str): The query parameter to be sent alongside the url.
        
        Returns:
            dict: A structured dictionary containing all of the information
                returned by the API.
                
        """
        query = self._remove_problem_characters(query)
        
        self._rate_limiting()

        resultQuery = requests.get(url.format(query),auth=(self.key,''))
        #200 is the authorised code for RESTful API calls
        if resultQuery.status_code == 200:
            result = json.JSONDecoder().decode(resultQuery.text)
        else:
            print(f"Failed with error code: {resultQuery.status_code} | "\
                  f"Reason: {resultQuery.reason}")
            result = {}
        
        return result
    
    def _rate_limiting(self):
        """Waits up to the defined time between requests.
        
        If more than the defined "time_between_requests" has passed (in 
        seconds) since the last call, this function will not wait any time.
        The last_request_timestamp class variable is reset to the current
        time every time this method is called.
        
        """
        if self.last_request_timestamp is None:
            self.last_request_timestamp = datetime.datetime.now()
            
        else:
            current_time = datetime.datetime.now()
            
            time_since_request = (current_time - 
                                  self.last_request_timestamp
                                  ).total_seconds()
            
            wait_time = max(self.time_between_requests - 
                            time_since_request,
                            0)
            
            time.sleep(wait_time)
            self.last_request_timestamp = datetime.datetime.now()   
            
    def _remove_problem_characters(self, string):
        """Remove invalid query parameters from the url query
        
        Spaces and the "&" sign will cause issues in an HTTP request so are
        replaced.
        
        Args:
            string (str): The query to be "cleaned".
            
        Returns:
            str: An equivalent string in HTTP GET format
        
        """
        string = string.replace(" ","+")
        string = string.replace("&","%26")
        
        return string
    
    def get_first_company_search(self, company_name):
        """Search for a company and return the top result.
        
        If no results are returned from the Companies House API then returns
        NoneType using a try block.
        
        Args:
            companyName (str): The company to search for.
            
        Returns:
            dict: The profile of the first result found from the API search.
        
        """
        search_result = self._query_ch_api(self.search_url, company_name)
        
        try: 
            first_result = search_result["items"][0]
        except IndexError:
            first_result = None
        
        return first_result
    
    def get_company_profile(self, company_number):
        """Return a company profile from the company number.
        
        Args:
            company_number (str): The unique company number as defined on
                Companies House.
                
        Returns:
            dict: The profile of the corresponding company
        
        """
        company_profile = self._query_ch_api(self.company_url, company_number)
        
        return company_profile
    
if __name__ == "__main__":
    key = "vLmk-4YxYS-QH8nMi8767zJSlcPlo3MKn41-d" #Fake key - insert your key here
    ch_api = CompaniesHouseService(key)
    iterations = 10
    
    tic = datetime.datetime.now()
    
    for company in range(iterations): 
        ch_profile = ch_api.get_company_profile("00445790")
        
    toc = datetime.datetime.now()
    
    time_taken = (toc - tic).total_seconds()
    print(f"Average time per iteration: "\
          f"{time_taken/(iterations-1):0.2f} seconds")