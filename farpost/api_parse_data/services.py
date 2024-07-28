from .models import Advertisement

class AdvertisementService:
    @staticmethod
    def create_advertisement(title, advertisement_id, author, views, position):
        return Advertisement.objects.create(
            title=title,
            advertisement_id=advertisement_id,
            author=author,
            views=views,
            position=position
        )

    @staticmethod
    def get_advertisement(advertisement_id):
        return Advertisement.objects.get(advertisement_id=advertisement_id)
