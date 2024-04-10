class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    # Create a property that returns the title of the article
    @property
    def title(self):
        return self._title

    # Create a setter method for the title property
    @title.setter
    def title(self, value):
        if (
            isinstance(value, str)
            and not hasattr(self, "title")
            and 5 <= len(value) <= 50
        ):
            self._title = value
        else:
            raise Exception

    # Create a property that returns the author of the article
    @property
    def author(self):
        return self._author

    # Create a setter method for the author property
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception

    # Create a property that returns the magazine of the article
    @property
    def magazine(self):
        return self._magazine

    # Create a setter method for the magazine property
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise Exception


class Author:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    # Create a property that returns the name of the author
    @property
    def name(self):
        return self._name

    # Create a setter method for the name property
    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, "name") and len(value) > 0:
            self._name = value
        else:
            raise Exception

    # Return a list of all articles written by the author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Returns a unique list of magazines for which the author has contributed to
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    # Create and return a new article written by the author
    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            return Article(self, magazine, title)

    # Returns a unique list of strings with the categories of the magazines the author has contributed to, else return None
    def topic_areas(self):
        if len(self.magazines()) > 0:
            return list(set([magazine.category for magazine in self.magazines()]))
        else:
            return None


class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    # Create a property that returns the name of the magazine
    @property
    def name(self):
        return self._name

    # Create a setter method for the name property
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise Exception

    # Create a property that returns the category of the magazine
    @property
    def category(self):
        return self._category

    # Create a setter method for the category property
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise Exception

    # Return a list of all articles published in the magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Returns a unique list of authors who have written for this magazine
    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    # Returns a list of the titles strings of all articles written for that magazine
    def article_titles(self):
        if len(self.articles()) > 0:
            return [article.title for article in self.articles()]
        else:
            return None

    # Returns a list of authors who have written more than 2 articles for the magazine
    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            if (len([article for article in self.articles() if article.author == author]) > 2):
                authors.append(author)
        if len(authors) > 0:
            return authors
        else:
            return None

    # Returns the Magazine instance with the most articles
    @classmethod
    def top_publisher(cls):
        if len(Article.all) > 0:
            # Using the max function with a lambda function to get the magazine with the most articles
            # The lambda function take an instance of the class called magazine
            # And returns the number of the articles for that instance
            # The max function will return the instance with the most articles
            return max(cls.all, key=lambda magazine: len(magazine.articles()))
        else:
            return None
