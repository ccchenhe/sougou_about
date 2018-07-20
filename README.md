## 搜狗请求加密部分

### suv生成方式
```sql
    suv = int(time.time()*1000)*1000 + random.randint(1, 1000)
```

### snuid生成方式
```sql
通过head请求获取到snuid,然后递归seed
```

1. snuid 失效期很长。
2. snuid 具体生成方式并未获取到，但可以持续seed的形式不断生成。
3. 请求时如果不携带snuid，搜狗会默认加上一个，以此来判断是否ban请求。
4. 一个snuid 用7~10次就可以扔掉。
