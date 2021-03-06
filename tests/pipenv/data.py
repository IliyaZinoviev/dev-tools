pipfile = '''
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
sqlalchemy = "<=1.3"
marshmallow = "*"

[dev-packages]
flake8 = "<4"

[requires]
python_version = "3.8"'''

pipfile_lock = '''
{
    "_meta": {
        "hash": {
            "sha256": "d099b218101e53edde5ce34ea434f0b8765687473ae0a661f63088a255d980ff"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.8"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "marshmallow": {
            "hashes": [
                "sha256:4ab2fdb7f36eb61c3665da67a7ce281c8900db08d72ba6bf0e695828253581f7",
                "sha256:eca81d53aa4aafbc0e20566973d0d2e50ce8bf0ee15165bb799bec0df1e50177"
            ],
            "index": "pypi",
            "version": "==3.10.0"
        },
        "sqlalchemy": {
            "hashes": [
                "sha256:04f995fcbf54e46cddeb4f75ce9dfc17075d6ae04ac23b2bacb44b3bc6f6bf11",
                "sha256:0c6406a78a714a540d980a680b86654feadb81c8d0eecb59f3d6c554a4c69f19",
                "sha256:0c72b90988be749e04eff0342dcc98c18a14461eb4b2ad59d611b57b31120f90",
                "sha256:108580808803c7732f34798eb4a329d45b04c562ed83ee90f09f6a184a42b766",
                "sha256:1418f5e71d6081aa1095a1d6b567a562d2761996710bdce9b6e6ba20a03d0864",
                "sha256:17610d573e698bf395afbbff946544fbce7c5f4ee77b5bcb1f821b36345fae7a",
                "sha256:216ba5b4299c95ed179b58f298bda885a476b16288ab7243e89f29f6aeced7e0",
                "sha256:2ff132a379838b1abf83c065be54cef32b47c987aedd06b82fc76476c85225eb",
                "sha256:314f5042c0b047438e19401d5f29757a511cfc2f0c40d28047ca0e4c95eabb5b",
                "sha256:318b5b727e00662e5fc4b4cd2bf58a5116d7c1b4dd56ffaa7d68f43458a8d1ed",
                "sha256:3ab5b44a07b8c562c6dcb7433c6a6c6e03266d19d64f87b3333eda34e3b9936b",
                "sha256:426ece890153ccc52cc5151a1a0ed540a5a7825414139bb4c95a868d8da54a52",
                "sha256:491fe48adc07d13e020a8b07ef82eefc227003a046809c121bea81d3dbf1832d",
                "sha256:4a84c7c7658dd22a33dab2e2aa2d17c18cb004a42388246f2e87cb4085ef2811",
                "sha256:54da615e5b92c339e339fe8536cce99fe823b6ed505d4ea344852aefa1c205fb",
                "sha256:5a7f224cdb7233182cec2a45d4c633951268d6a9bcedac37abbf79dd07012aea",
                "sha256:61628715931f4962e0cdb2a7c87ff39eea320d2aa96bd471a3c293d146f90394",
                "sha256:62285607a5264d1f91590abd874d6a498e229d5840669bd7d9f654cfaa599bd0",
                "sha256:62fb881ba51dbacba9af9b779211cf9acff3442d4f2993142015b22b3cd1f92a",
                "sha256:68428818cf80c60dc04aa0f38da20ad39b28aba4d4d199f949e7d6e04444ea86",
                "sha256:6aaa13ee40c4552d5f3a59f543f0db6e31712cc4009ec7385407be4627259d41",
                "sha256:70121f0ae48b25ef3e56e477b88cd0b0af0e1f3a53b5554071aa6a93ef378a03",
                "sha256:715b34578cc740b743361f7c3e5f584b04b0f1344f45afc4e87fbac4802eb0a0",
                "sha256:758fc8c4d6c0336e617f9f6919f9daea3ab6bb9b07005eda9a1a682e24a6cacc",
                "sha256:7d4b8de6bb0bc736161cb0bbd95366b11b3eb24dd6b814a143d8375e75af9990",
                "sha256:81d8d099a49f83111cce55ec03cc87eef45eec0d90f9842b4fc674f860b857b0",
                "sha256:888d5b4b5aeed0d3449de93ea80173653e939e916cc95fe8527079e50235c1d2",
                "sha256:95bde07d19c146d608bccb9b16e144ec8f139bcfe7fd72331858698a71c9b4f5",
                "sha256:9bf572e4f5aa23f88dd902f10bb103cb5979022a38eec684bfa6d61851173fec",
                "sha256:bab5a1e15b9466a25c96cda19139f3beb3e669794373b9ce28c4cf158c6e841d",
                "sha256:bd4b1af45fd322dcd1fb2a9195b4f93f570d1a5902a842e3e6051385fac88f9c",
                "sha256:bde677047305fe76c7ee3e4492b545e0018918e44141cc154fe39e124e433991",
                "sha256:c389d7cc2b821853fb018c85457da3e7941db64f4387720a329bc7ff06a27963",
                "sha256:d055ff750fcab69ca4e57b656d9c6ad33682e9b8d564f2fbe667ab95c63591b0",
                "sha256:d53f59744b01f1440a1b0973ed2c3a7de204135c593299ee997828aad5191693",
                "sha256:f115150cc4361dd46153302a640c7fa1804ac207f9cc356228248e351a8b4676",
                "sha256:f1e88b30da8163215eab643962ae9d9252e47b4ea53404f2c4f10f24e70ddc62",
                "sha256:f8191fef303025879e6c3548ecd8a95aafc0728c764ab72ec51a0bdf0c91a341"
            ],
            "index": "pypi",
            "version": "==1.3.22"
        }
    },
    "develop": {
        "flake8": {
            "hashes": [
                "sha256:749dbbd6bfd0cf1318af27bf97a14e28e5ff548ef8e5b1566ccfb25a11e7c839",
                "sha256:aadae8761ec651813c24be05c6f7b4680857ef6afaae4651a4eccaef97ce6c3b"
            ],
            "index": "pypi",
            "version": "==3.8.4"
        },
        "mccabe": {
            "hashes": [
                "sha256:ab8a6258860da4b6677da4bd2fe5dc2c659cff31b3ee4f7f5d64e79735b80d42",
                "sha256:dd8d182285a0fe56bace7f45b5e7d1a6ebcbf524e8f3bd87eb0f125271b8831f"
            ],
            "version": "==0.6.1"
        },
        "pycodestyle": {
            "hashes": [
                "sha256:2295e7b2f6b5bd100585ebcb1f616591b652db8a741695b3d8f5d28bdc934367",
                "sha256:c58a7d2815e0e8d7972bf1803331fb0152f867bd89adf8a01dfd55085434192e"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "version": "==2.6.0"
        },
        "pyflakes": {
            "hashes": [
                "sha256:0d94e0e05a19e57a99444b6ddcf9a6eb2e5c68d3ca1e98e90707af8152c90a92",
                "sha256:35b2d75ee967ea93b55750aa9edbbf72813e06a66ba54438df2cfac9e3c27fc8"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "version": "==2.2.0"
        }
    }
}
'''

test_pipfile = \
    '''[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
sqlalchemy = "==1.*"
marshmallow = "==3.*"

[dev-packages]
flake8 = "==3.*"

[requires]
python_version = "3.8"'''

test_pipfile_only_unlocked = \
    '''[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
sqlalchemy = "<=1.3"
marshmallow = "==3.*"

[dev-packages]
flake8 = "<4"

[requires]
python_version = "3.8"'''


test_pipfile_minor = \
    '''[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
sqlalchemy = "==1.3.*"
marshmallow = "==3.10.*"

[dev-packages]
flake8 = "==3.8.*"

[requires]
python_version = "3.8"'''

test_pipfile_only_unlocked_and_minor = \
    '''[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
sqlalchemy = "<=1.3"
marshmallow = "==3.10.*"

[dev-packages]
flake8 = "<4"

[requires]
python_version = "3.8"'''


test_pipfile_fix = \
    '''[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
sqlalchemy = "==1.3.22"
marshmallow = "==3.10.0"

[dev-packages]
flake8 = "==3.8.4"

[requires]
python_version = "3.8"'''

test_pipfile_only_unlocked_and_fix = \
    '''[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
sqlalchemy = "<=1.3"
marshmallow = "==3.10.0"

[dev-packages]
flake8 = "<4"

[requires]
python_version = "3.8"'''