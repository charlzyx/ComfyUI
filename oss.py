from minio import Minio

bucket_name = "comfyui"
entrypoint = "127.0.0.1:9000"
client = Minio(
    entrypoint,
    access_key="puPJLcGNjSe2HurDhyId",
    secret_key="Yf4HpYscAEkjNlYYi9lGabM3jSzUvoBtZGS7X6gs",
    secure=False,
)


def oss_image_save(filename, filebytes):
    client.put_object(
        bucket_name,
        filename,
        filebytes,
        # 10 MiB
        part_size=8 * 1024 * 1024,
        length=-1,
    )

    return "/".join(["//" + entrypoint, bucket_name, filename])


# oss_image_save("test", "./pytest.ini")
