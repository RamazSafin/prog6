import random
from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

categories = {
    "cats": [
        "https://avatars.mds.yandex.net/i?id=11abb9edc03f3df6f30b3017ae36457a65528f2e-10157084-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=b8d9712e51cd959eb217591962e7cacd57e08ebf-12752514-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=c28004056ab97f9a99f8ed8a835f68b591f7e52c-12803937-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=8b29be103171826a8a9b44cfed821c8d1bd8f181-11532301-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=11795f7dd85d485a4c8506a893386462207a75e0-12639726-images-thumbs&n=13"

    ],
    "dogs": [
        "https://avatars.mds.yandex.net/i?id=a8ee34af3c8f8c4e343b12b72962e50ca7e7d6dd-12011291-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=4ae4958dd50c4e3d4dc254c21ba5dc91e0f2a666-5209664-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=7fc99204a03f2358756ca5b76069d110613d56bf-12159448-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=1605c387f7c37c31ccd80696b5efcdfe9836dc0d-12645377-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=b085ac66691a23cd3c1519eef80a36e74713c12a-4493789-images-thumbs&n=13"
    ],
    "nature": [
        "https://avatars.mds.yandex.net/i?id=3b9046e1bf59dafc2008a57d98d57916e42fa06a-9863853-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=3096f7fe888be99aac7db102a995aee2aaf5436a-12601053-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=b3fbc178464ff0e97e3a0509f9326ff3ecc1b3e5-12497179-images-thumbs&n=13",
    ]
}

@app.get("/random_image/")
async def get_random_image(category: Optional[str] = None):
    if category:
        if category in categories:
            # Возвращаем случайное изображение из указанной категории
            return {"image_url": random.choice(categories[category])}
        else:
            raise HTTPException(status_code=404, detail="Category not found")
    else:
        # Если категория не указана, выбираем случайную категорию и возвращаем случайное изображение из нее
        random_category = random.choice(list(categories.keys()))
        return {"category": random_category, "image_url": random.choice(categories[random_category])}
