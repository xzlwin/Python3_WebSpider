"""
font_face: 第一次进入网页时的字体编码. 用于生成01.ttf文件.
font_face_2: 第二次进入网页（或者刷新网页）后得到的字体编码. 用于生成02.ttf

注意：b64decode()、open()函数请灵活改变, 便于生成不同的ttf文件,在此不再叙述.
"""

import base64

font_face = 'd09GRgABAAAAAAgkAAsAAAAAC7gAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABHU1VCAAABCAAAADMAAABCsP6z7U9TLzIAAAE8AAAARAAAAFZW7la5Y21hcAAAAYAAAAC9AAACTC2JhkBnbHlmAAACQAAAA5IAAAQ0l9+jTWhlYWQAAAXUAAAALwAAADYS8aYMaGhlYQAABgQAAAAcAAAAJAeKAzlobXR4AAAGIAAAABIAAAAwGhwAAGxvY2EAAAY0AAAAGgAAABoGXgUabWF4cAAABlAAAAAfAAAAIAEZADxuYW1lAAAGcAAAAVcAAAKFkAhoC3Bvc3QAAAfIAAAAXAAAAI/ISNjHeJxjYGRgYOBikGPQYWB0cfMJYeBgYGGAAJAMY05meiJQDMoDyrGAaQ4gZoOIAgCKIwNPAHicY2Bk0mWcwMDKwMHUyXSGgYGhH0IzvmYwYuRgYGBiYGVmwAoC0lxTGBwYKr47Mev812GIYdZhuAIUZgTJAQDcOgtLeJzFkrENgzAQRb8DIQkEKSVDhCWQGIFdmCATZAM2SEN6JkEusEBCdIiKfHM0kaBNznqW7mzfne4bwBGAQ+7EBdQbCtZejKol7sBf4i4e9CPcGDkjr0sdNpkpzNTGne6rIR2TeeaN/ZMtU8y4tezJgTV9BOzxghM8VmWnytvJ9ANT/yv9bddlf65eQPIVtliXAucHHQpW2yYTrJ6mEOxbMwn2L7SxwImj0wJnj74SqAKGVKAeGBMBzgfqVUREAAAAeJxFk81v2mYcx5/HVDgllJBi40JawEBsY5Lg+I0AjqEQaPPKSIAQ0tIQtZRma5tFTZe20dayF6md9ge0l0o77FLt0HsnTetpa9XmsD9g0q67rVIvEeyxgzIfHul5pMef78vvARCA3j9ABATAAIhLJOEjOIA+aC4fsfcgDMAoSctx3RLXYVyVmVDQirM6FN0kYcUdEHdYcPixyw7aRrgEkyySkXktvQDrJ/fe7dFRIidwInV6oFz2+zyxmBIQ5s5NXZudK9haN3Yq44silebo8TPUKYRDCnofYBcxA2AM0RkWsXCDQepQMngOGAoyihxXJZFyU5DwoWNVkZmgFT6zk2GZD/CU/VRgXVrdT17N3nqykPu8oir27lM2z6il4t0y5papUcqfOLeiTk50Wrk7089fHTSWhYly981YJVpfnF2tGjoQ/RB7C2wA6aIVWoHSsESGSHbYAnPdP2DhYrNZ++tFCR50hdKLQ3T2y1FmvX9hD+mPoixNbbJpIU6ZKs3gVFO8D6LsfBAliAyxnaELql5hI5o3bHMk1tKqNGOrORPJclKcVMTJ9IXH7Sv7J3+fz1b3Wc62CFPTQlrPDtVjk94ztY1599ClwuWvt+v/97aLNNiR8tAw6kdRjeIkuFsLtLnZqRFuMIEJPs1ZCYoegTq+08NeAxcALoUmUaNWPGS0bdyMwYNQbkZyeQbW4bDTn/JlaOxWJR9u3nuQqX/Kt7S924lLTN//B+wE9hvwH/s/Mu2iSRrvd4gjyyzDfmebVTO1ai6aI1by8Gr3bzYwE2o8SuS/2JzWB17ns5tPq4zfBrfLv7qpR9c3Lq6qU/X+jGAA+QuBWJ+CNOpwGsqs1fg3mg+UsJGtMS2IBE0RJEG5RfX7QU3gU6zDikNPbCy+dv+rzZldLXW3WJFVG2wvT6WqEf5e8WdNGdUVrzoycMLKe70Pt25+O/9D58mPlYlYBaYW1hpLhUh0FRzP7CHSQxiuXeidQHM4+6/DUBAnENnJMmiWeY+3vbSTOut02h0j14rXtUK9dH+F5x6Ex2GzM7dUXucz2s10i11amau9eXlnF26kklIWAMuxb4MzjkiGTzNPc4wQBu0RSRKNNxq0WgikATVwtHv52farna1svvPn+UxByMpCiM61zp8NjgYjAYmMlL8swW+4rU9u3F5oc+4r2cv7utYsNH6S0wF/I5fpPmbzhIsk2IfLJQD+Awzo4MIAAHicY2BkYGAA4lnXD2nG89t8ZeBmYQCB6y8NtRD0/zcsDEzngVwOBiaQKAA+WQsNAHicY2BkYGDW+a/DEMPCAAJAkpEBFfAAADNiAc14nGNhAIIUBgYmHeIwADeMAjUAAAAAAAAADABGAIoApgDoAQIBJgFYAaAB1AIaAAB4nGNgZGBg4GEwYGBmAAEmIOYCQgaG/2A+AwAOgwFWAHicZZG7bsJAFETHPPIAKUKJlCaKtE3SEMxDqVA6JCgjUdAbswYjv7RekEiXD8h35RPSpcsnpM9grhvHK++eOzN3fSUDuMY3HJyee74ndnDB6sQ1nONBuE79SbhBfhZuoo0X4TPqM+EWungVbuMGb7zBaVyyGuND2EEHn8I1XOFLuE79R7hB/hVu4tZpCp+h49wJt7BwusJtPDrvLaUmRntWr9TyoII0sT3fMybUhk7op8lRmuv1LvJMWZbnQps8TBM1dAelNNOJNuVt+X49sjZQgUljNaWroyhVmUm32rfuxtps3O8Hort+GnM8xTWBgYYHy33FeokD9wApEmo9+PQMV0jfSE9I9eiXqTm9NXaIimzVrdaL4qac+rFWGMLF4F9qxlRSJKuz5djzayOqlunjrIY9MWkqvZqTRGSFrPC2VHzqLjZFV8af3ecKKnm3mCH+A9idcsEAeJxtyjsOgCAURNE3+EER94KCQUtQ2IuNnYnLNz5apzm5yZCgMkX/0xCoUKNBC4kOPRQGaIyER97XmaboP7N3M7c1B7vmjU27ZWNis3ELd5jLzy+l12CJXh54F6E='
font_face_2 = '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'
b = base64.b64decode(font_face_2)
with open('02.ttf', 'wb') as f:
    f.write(b)