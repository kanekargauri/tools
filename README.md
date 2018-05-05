# tools
supporting tools

#### generate unique string for distributed system
```
>>> import url_slug_util
>>> print url_slug_util.generate_unique()
hj398002yk3f31u
>>> print url_slug_util.generate_unique(15)
6gydezq8l35h1833cauv
```

#### combine strings to make it url compatible
```
>>> import url_slug_util
>>> url_slug_util.build_url_compatible('hello', 'world')
'hello-world'
>>> print url_slug_util.build_url_compatible('गब्बर', 'सिंग')
गब्बर-सिंग
>>> url_slug_util.build_url_compatible('this is    1243  head', '&&& line @@  ---- ')
'this-is-1243-head-line'
>>> url_slug_util.build_url_compatible('hello  world')
'hello-world'
```

