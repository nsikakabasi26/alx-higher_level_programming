#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as ad
    ad.add.a = 1
    ad.add.b = 2
    val = ad.add(ad.add.a, ad.add.b)
    print("{} + {} = {}".format(ad.add.a, ad.add.b, val))
