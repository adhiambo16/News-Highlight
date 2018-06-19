class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://newsapi.org/v2/top-headlines/everything?apiKey={58ffdf91c72b4fccb8d745405b739de3'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


    
  

   


