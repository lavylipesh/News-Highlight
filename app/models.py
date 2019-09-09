class Sources:
    '''
    class that defines sources object
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        
class Articles:
    '''
    class that defines article object
    '''
    def __init__(self,source,author,title,description,url,image,time):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = time
        self.content = content

