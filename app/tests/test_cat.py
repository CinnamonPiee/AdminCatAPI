import pytest


@pytest.mark.asyncio
async def test_get_empty_breeds(client, setup_database):
    response = await client.get("/breeds/")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_create_kitten(client, setup_database):
    breed_data = {"name": "Siamese"}
    response = await client.post("/breeds/", json=breed_data)
    assert response.status_code == 200
    breed = response.json()
    assert breed["name"] == "Siamese"

    kitten_data = {
        "name": "Kitty",
        "color": "White",
        "age": 4,
        "description": "A cute white Siamese kitten",
        "breed_id": breed["id"]
    }
    response = await client.post("/kitten/", json=kitten_data)
    assert response.status_code == 200
    kitten = response.json()
    assert kitten["name"] == "Kitty"
    assert kitten["color"] == "White"
    assert kitten["age"] == 4


@pytest.mark.asyncio
async def test_get_kitten(client, setup_database):
    response = await client.get("/kitten/1")
    assert response.status_code == 200
    kitten = response.json()
    assert kitten["name"] == "Kitty"


@pytest.mark.asyncio
async def test_update_kitten(client, setup_database):
    updated_data = {
        "name": "Updated Kitty",
        "color": "Black",
        "age": 5,
        "description": "A cute black Siamese kitten"
    }
    response = await client.put("/kitten/1", json=updated_data)
    assert response.status_code == 200
    updated_kitten = response.json()
    assert updated_kitten["name"] == "Updated Kitty"
    assert updated_kitten["color"] == "Black"
    assert updated_kitten["age"] == 5


@pytest.mark.asyncio
async def test_delete_kitten(client, setup_database):
    response = await client.delete("/kitten/1")
    assert response.status_code == 200
    deleted_kitten = response.json()
    assert deleted_kitten["name"] == "Updated Kitty"

    response = await client.get("/kitten/1")
    assert response.status_code == 404
