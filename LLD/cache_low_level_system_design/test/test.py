from cache_low_level_system_design.src.cache import Cache


if __name__ == "__main__":
    cache = Cache(capacity=2)

    cache.put('id::1', 1)
    cache.put('id::2', 2)

    print(cache.get('id::1'))
    cache.put('id::3', 3)
    print(cache.get('id::3'))
