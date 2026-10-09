class ArticleTagSystem:
    def __init__(self):
        self.articles={}
        self.tag_index={}


    def add_article(self,article_id,tags):
        self.articles[article_id]=set(tags)

        for tag in tags:
            if tag not in self.tag_index:
                self.tag_index[tag] = set()
            self.tag_index[tag].add(article_id)
    def get_article_with_tag(self,tag):
        return self.tag_index.get(tag, set())
    def get_all_tags(self):
        # return set(self.tag_index.keys())
        get_tags=list(self.tag_index.keys())
        for i,tag in enumerate(get_tags):
            print(f"{i+1}:{tag}")
        return get_tags
TagSystem= ArticleTagSystem()
list_tags=TagSystem.get_all_tags()
TagSystem.add_article(1,["python","coding"])
TagSystem.add_article(2,["python","data science"])
get_index_tag=int(input("Enter the index of the tag you want to see articles for: "))
print(f"{TagSystem.get_article_with_tag(list_tags[get_index_tag-1])}")

# print(TagSystem.get_article_with_tag("python"))  # Output: {1, 2}
# print(TagSystem.get_all_tags())  # Output: {'python', 'coding', 'data science'}