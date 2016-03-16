from models import PostStatistic
from vkontakte_wall.factories import PostFactory
import factory


class PostStatisticFactory(factory.DjangoModelFactory):
    post = factory.SubFactory(PostFactory)

    class Meta:
        model = PostStatistic
