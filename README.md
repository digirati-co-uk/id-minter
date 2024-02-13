# id-minter
User-friendly identifier generator in various languages, based on Wellcome's Scala version:

https://github.com/wellcomecollection/catalogue-pipeline/blob/main/pipeline/id_minter/src/main/scala/weco/pipeline/id_minter/utils/Identifiable.scala

Background:

https://github.com/wellcomecollection/catalogue-pipeline/blob/main/pipeline/id_minter/README.md


Example - from dotnet

```
Identifiable.Generate()
gz2ewdch
yn9r7pq7
mj8239ts
eghrt6cb
nw6yz8tk
kjjrhkp4
jpfeq3z8
h34zh7ya
ta3mh4as
t5ex6986
```

```
Identifiable.Generate(length:16)
ya2kr3ta7ugkts8r
q74pcvwhmyqbgv7v
aupbm9bgsewaffvs
e7emvqn2ysb975qw
zy3dbcc729hhwzsh
ydq3mst5phvumjye
r7x2epzpckb4p54r
haswxtagebcxv6fh
m48r66prgdf6nnj3
tpb7sqyhp5zba4uq
```

```
Identifiable.Generate(letterFirst:false)
qwpmnf44
2gsp29ya
yd5fnafj
85zpevr7
eykhqwat
puw5eg7u
pty44ees
z6dcc9pd
69j8y322
qm7ufgyg
```
