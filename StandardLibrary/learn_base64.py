"""
Learn base64
https://docs.python.org/3/library/base64.html?highlight=base64#module-base64

Base64是一种用64个字符来表示任意二进制数据的方法

    用记事本打开exe, jpg, pdf这些文件时, 我们都会看到一大堆乱码
    因为二进制文件包含很多无法显示和打印的字符
    所以, 如果要让记事本这样的文本处理软件能处理二进制数据, 就需要一个二进制到字符串的转换方法. 
    Base64是一种最常见的二进制编码方法

Base64的原理很简单
    首先, 准备一个包含64个字符的数组: 
        ["A", "B", "C", ... "a", "b", "c", ... "0", "1", ... "+", "/"]
    然后, 对二进制数据进行处理, 每3个字节一组, 一共是3x8=24bit, 划为4组, 每组正好6个bit
    这样我们得到4个数字作为索引, 然后查表, 获得相应的4个字符, 就是编码后的字符串
    所以, Base64编码会把3字节的二进制数据编码为4字节的文本数据, 长度增加33%, 
        好处是编码后的文本数据可以在邮件正文, 网页等直接显示
    如果要编码的二进制数据不是3的倍数, 最后会剩下1个或2个字节怎么办? 
        Base64用\x00字节在末尾补足后, 
        再在编码的末尾加上1个或2个=号, 表示补了多少字节, 解码的时候, 会自动去掉


base64 使用
    由于标准的Base64编码后可能出现字符+和/, 在URL中就不能直接作为参数, 
        所以又有一种"url safe"的base64编码, 其实就是把字符+和/分别变成-和_
    还可以自己定义64个字符的排列顺序, 这样就可以自定义Base64编码, 不过, 通常情况下完全没有必要
    Base64是一种通过查表的编码方法, 不能用于加密, 即使使用自定义的编码表也不行. 
    Base64适用于小段内容的编码, 比如数字证书签名, Cookie的内容等
"""


import base64

print(base64.b64encode(b"binary\x00string"))
# >>> b"YmluYXJ5AHN0cmluZw=="
print(base64.b64decode(b"YmluYXJ5AHN0cmluZw=="))
# >>> b"binary\x00string"


print("\nurl safe")
print(base64.b64encode(b"i\xb7\x1d\xfb\xef\xff"))
# >>> b"abcd++//"
print(base64.urlsafe_b64encode(b"i\xb7\x1d\xfb\xef\xff"))
# >>> b"abcd--__"
print(base64.urlsafe_b64decode("abcd--__"))
# >>> b"i\xb7\x1d\xfb\xef\xff"

# 由于=字符也可能出现在Base64编码中, 但=用在URL, Cookie里面会造成歧义, 所以, 很多Base64编码后会把=去掉
# 去掉=后怎么解码呢? 
    # 因为Base64是把3个字节变为4个字节, 所以, Base64编码的长度永远是4的倍数, 
    # 因此, 需要加上=把Base64字符串的长度变为4的倍数, 就可以正常解码了
print(base64.b64encode(b"abcd")) # >>> b"YWJjZA=="  # 带等号

def safe_base64_decode(s):
    if isinstance(s, bytes):
        if s[-2:] == b"==" or s[-1] == b"=":
            return base64.b64decode(s)
        else:
            s = s + b"=="
            return base64.b64decode(s)

assert b"abcd" == safe_base64_decode(b"YWJjZA=="), "safe_base64_decode('YWJjZA==')"
assert b"abcd" == safe_base64_decode(b"YWJjZA"), "safe_base64_decode('YWJjZA')"
print("ok")


with open("./temp/b64test.xlsx", "rb") as bo:
    content = bo.read()
    print(base64.b16encode(content))

# >>> b"504B03041400060008000000210062EE9D685E01000090040000130008025B436F6E74656E745F54797065735D2E786D6C20A2040228A000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000AC94CB4EC3301045F748FC43E42D4ADCB2400835ED82C7122A513EC0C493C6AA635B9E6969FF9E89FB1042A1156A37B112CFDC7B32F1CD68B26E6DB68288C6BB520C8B81C8C0555E1B372FC5C7EC25BF171992725A59EFA0141B4031195F5F8D669B009871B7C3523444E1414AAC1A6815163E80E39DDAC75611DFC6B90CAA5AA839C8DBC1E04E56DE1138CAA9D310E3D113D46A69297B5EF3E32D49048B227BDC16765EA550215853296252B972FA974BBE7328B833D5606302DE308690BD0EDDCEDF06BBBE371E4D341AB2A98AF4AA5AC6906B2BBF7C5C7C7ABF288E8BF450FABA3615685F2D5B9E40812182D2D800506B8BB416AD326ECF7DC43F15A34CCBF0C220DDFB25E1131CC4DF1B64BA9E8F90644E18226D2CE0A5C79E444F39372A827EA7C8C9B838C04FED631C7C6EA6D107E40445F8FF14F611E9BAF3C04210C9C021247D87EDE0C8E93B7BECD0E55B83EEF196E97F32FE060000FFFF0300504B030414000600080000002100B5553023F40000004C0200000B0008025F72656C732F2E72656C7320A2040228A000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000AC924D4FC3300C86EF48FC87C8F7D5DD9010424B774148BB21547E8049DC0FB58DA3241BDDBF271C10541A8303477FBD7EFCCADBDD3C8DEAC821F6E234AC8B12143B23B677AD8697FA7175072A2672964671ACE1C41176D5F5D5F699474A792876BD8F2AABB8A8A14BC9DF2346D3F144B110CF2E571A0913A51C86163D99815AC64D59DE62F8AE01D54253EDAD86B0B737A0EA93CF9B7FD796A6E90D3F88394CECD29915C8736267D9AE7CC86C21F5F91A5553683969B0629E723A22795F646CC0F3449BBF13FD7C2D4E9CC852223412F832CF47C725A0F57F5AB434F1CB9D79C43709C3ABC8F0C9828B1FA8DE010000FFFF0300504B030414000600080000002100813E9497F3000000BA0200001A000801786C2F5F72656C732F776F726B626F6F6B2E786D6C2E72656C7320A2040128A0000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000AC524D4BC43010BD0BFE8730779B761511D9742F22EC55EB0F08C9B429DB2621337EF4DF1B2ABA5D58D64B2F036F8679EFCDC776F7350EE20313F5C12BA88A12047A136CEF3B056FCDF3CD030862EDAD1E8247051312ECEAEBABED0B0E9A7313B93E92C82C9E1438E6F828251987A3A62244F4B9D286346ACE3075326A73D01DCA4D59DECBB4E480FA8453ECAD82B4B7B7209A2966E5FFB943DBF6069F82791FD1F31909493C0D7900D1E8D4212BF8C145F608F2BCFC664D79CE6BC1A3FA0CE51CAB4B1EAA353D7C86742087C8471F7F299273E5A299BB55EFE17442FBCA29BFDBF22CCBF4EF66E4C9C7D5DF000000FFFF0300504B030414000600080000002100779BFDB086020000AF0500000F000000786C2F776F726B626F6F6B2E786D6CAC54DB4EE330107D5F69FF21F27B48EC5C5AA2A60868D05662576861E11119C76DAC267164BB6D2AC4BFEF382185C24BC56E94786C4F7CE6CCC533396BABD2D970A585AC53844F7CE4F09AC95CD4CB14FDB9BB72C7C8D186D6392D65CD53B4E31A9D4DBF7F9B6CA55A3D49B97200A0D6292A8C6912CFD3ACE015D527B2E13568165255D4C0522D3DDD284E735D706EAAD223BE1F7B151535EA1112750C865C2C04E333C9D615AF4D0FA278490DD0D78568F48056B163E02AAA56EBC665B26A00E24994C2EC3A50E4542C992F6BA9E853096EB738725A056F0C1FF661208325507D325509A6A4960B7302D05E4FFA93FFD8F7303E0841FB3906C721859EE21B6173B867A5E22FB28AF758F11B18F6FF190D436975B59240F0BE8816EDB911349D2C44C9EFFBD27568D3FCA295CD54899C926A93E5C2F03C452358CA2D3FD850EBE6622D4AD0127F14F8C89BEECBF94639006BB8BA516243D90EEE8455B72A19227C639403F3F9EC1AACDCD20DD804CFF2D7929C03280E1E6BA612FCF81C671921571971B3EC1CBBE1781CB9E3280EDD088FE2CB0C076382E317088B8A1326E9DA14AFEE58E8140536011F553F693B68B09FAC45FE46E3D97F7D5C2B3F0C83EEC5BA632FEEBDE05BFDE6B85D3AED83A873B9ED3CDABD9B6FBBED07919B026246480CCCFABD1F5C2C0BE08A491C46962EB19C5274C065D673B982C7B5C30117EF1D99AE3900A94E3A7597D05BDB303074212BBBF0224725D6869AE75D72BCE118A32583045AD1FD1893531C587F796BAEB5E9A4B35602E8E1D03F1FF9A7A1EB674104993925EE380C887B19CE48168DB2597611D9CCD8E696FC8F2B0E3584A364E89A96654195B95394ADA0D7FEE68B0BAAA1947A8780EF74E20DACBDE1D4F42F000000FFFF0300504B030414000600080000002100053CDBAAA2000000D300000014000000786C2F736861726564537472696E67732E786D6C5C8E410AC2301045F7827708B3B7A90A2292A40BC113E801623BDA4033A999A9E8ED8D88082EDFFB3CF8A679C441DD317348646159D5A090DAD405BA5A381D0F8B2D28164F9D1F12A1852732346E3E33CCA24A4B6CA11719775A73DB63F45CA511A92C9794A39782F9AA79CCE83BEE11250E7A55D71B1D7D20506D9A482CAC414D146E13EEBFEC0C0767C479A3C519FD868F38FF8BF6277439E55E000000FFFF0300504B030414000600080000002100753E9969930600008C1A000013000000786C2F7468656D652F7468656D65312E786D6CEC595B8BDB46147E2FF43F08BD3BBE49B2BDC41B6CD94EDAEC2621EBA4E4716C8FADC98E344633DE8D0981923CF5A550484B5F0A7DEB43290D34D0D097FE98858436FD113D3392AD99F5389BCBA6B4256B58A4D177CE7C73CED137175DBC742FA6CE114E396149DBAD5EA8B80E4EC66C429259DBBD351C949AAEC3054A2688B204B7DD25E6EEA5DD8F3FBA8876448463EC807DC27750DB8D8498EF94CB7C0CCD885F60739CC0B3294B6324E0369D9527293A06BF312DD72A95A01C2392B84E8262707B7D3A2563EC0CA54B7777E5BC4FE136115C368C697A205D63C3426127875589E04B1ED2D43942B4ED423F13763CC4F784EB50C4053C68BB15F5E796772F96D14E6E44C5165BCD6EA0FE72BBDC607258537DA6B3D1BA53CFF3BDA0B3F6AF00546CE2FA8D7ED00FD6FE14008DC730D28C8BEED3EFB6BA3D3FC76AA0ECD2E2BBD7E8D5AB065EF35FDFE0DCF1E5CFC02B50E6DFDBC00F062144D1C02B5086F72D3169D442CFC02B50860F36F08D4AA7E7350CBC02459424871BE88A1FD4C3D568D79029A357ACF096EF0D1AB5DC7981826A585797EC62CA12B1ADD6627497A5030048204582248E58CEF1148DA18A4344C92825CE1E994550787394300ECD955A6550A9C37FF9F3D4958A08DAC148B396BC8009DF68927C1C3E4EC95CB4DD4FC1ABAB419E3F7B76F2F0E9C9C35F4F1E3D3A79F873DEB77265D85D41C94CB77BF9C3577F7DF7B9F3E72FDFBF7CFC75D6F5693CD7F12F7EFAE2C56FBFBFCA3D8CB808C5F36F9EBC78FAE4F9B75FFEF1E3638BF74E8A463A7C4862CC9D6BF8D8B9C96218A0853F1EA56F66318C10312C5004BE2DAEFB223280D79688DA705D6C86F0760A2A63035E5EDC35B81E44E942104BCF57A3D800EE3346BB2CB506E0AAEC4B8BF07091CCEC9DA70B1D7713A1235BDF214A8C04F71773905762731946D8A07983A244A0194EB070E4337688B16574770831E2BA4FC629E36C2A9C3BC4E922620DC9908C8C422A8CAE9018F2B2B41184541BB1D9BFED7419B58DBA878F4C24BC16885AC80F3135C278192D048A6D2E8728A67AC0F790886C240F96E958C7F5B9804CCF30654E7F8239B7D95C4F61BC5AD2AF82C2D8D3BE4F97B1894C0539B4F9DC438CE9C81E3B0C2314CFAD9C4912E9D84FF8219428726E306183EF33F30D91F79007946C4DF76D828D749F2D04B7405C754A4581C8278BD492CBCB9899EFE3924E11562A03DA6F487A4C9233F5FD94B2FBFF8CB2DB35FA1C34DDEEF85DD4BC9312EB3B75E594866FC3FD0795BB8716C90D0C2FCBE6CCF541B83F08B7FBBF17EE6DEFF2F9CB75A1D020DEC55A5DADDCE3AD0BF729A1F4402C29DEE36AEDCE615E9A0CA0516D2AD4CE72BD919B4770996F130CDC2C45CAC64999F88C88E820427358E057D53674C673D733EECC198775BF6A561B627CCAB7DA3D2CE27D36C9F6ABD5AADC9B66E2C19128DA2BFEBA1DF61A2243078D620FB676AF76B533B5575E1190B66F4242EBCC2451B79068AC1A210BAF22A146762E2C5A16164DE97E95AA5516D7A1006AEBACC0C2C981E556DBF5BDEC1C00B65488E289CC537624B0CAAE4CCEB9667A5B30A95E01B08A58554091E996E4BA7578727459A9BD46A60D125AB99924B4328CD004E7D5A91F9C9C67AE5B454A0D7A3214ABB7A1A0D168BE8F5C4B1139A50D34D1958226CE71DB0DEA3E9C8D8DD1BCED4E61DF0F97F11C6A87CB052FA233383C1B8B347BE1DF4659E629173DC4A32CE04A7432358889C0A94349DC76E5F0D7D54013A5218A5BB50682F0AF25D70259F9B79183A49B49C6D3291E0B3DED5A8B8C74760B0A9F6985F5A9327F7BB0B4640B48F741343976467491DE4450627EA32A0338211C8E7FAA59342704CE33D74256D4DFA98929975DFD4051D550D68EE83C42F98CA28B79065722BAA6A3EED631D0EEF23143403743389AC909F69D67DDB3A76A19394D348B39D35015396BDAC5F4FD4DF21AAB6212355865D2ADB60DBCD0BAD64AEBA050ADB3C419B3EE6B4C081AB5A233839A64BC29C352B3F35693DA392E08B448045BE2B69E23AC9178DB991FEC4E57AD9C2056EB4A55F8EAC387FE6D828DEE8278F4E01478410557A9842F0F2982455F768E9CC906BC22F744BE46842B679192B67BBFE277BCB0E687A54AD3EF97BCBA572935FD4EBDD4F1FD7AB5EF572BBD6EED014C2C228AAB7EF6D16500075174997F7A51ED1B9F5FE2D559DB85318BCB4C7D5E292BE2EAF34BB5B6FDF38B434074EE07B541ABDEEA06A556BD332879BD6EB3D40A836EA917848DDEA017FACDD6E081EB1C29B0D7A9875ED06F96826A1896BCA022E9375BA58657AB75BC46A7D9F73A0FF2650C8C3C938F3C16105EC56BF76F000000FFFF0300504B03041400060008000000210079A1806CA4020000520600000D000000786C2F7374796C65732E786D6CA4556D6BDB3010FE3ED87F10FAEECA76E32C09B6CBD2D450E8C6A01DECAB62CB89A85E8C2467CEC6FEFB4E765E1C3AB6D17E894EE7D373CFDD7352D29B4E0AB463C672AD321C5D85183155EA8AAB4D86BF3E15C10C23EBA8AAA8D08A6578CF2CBEC9DFBF4BADDB0BF6B865CC21805036C35BE79A0521B6DC3249ED956E98822FB536923AD89A0DB18D61B4B2FE9014240EC32991942B3C202C64F93F20929AE7B6094A2D1BEAF89A0BEEF63D1646B25CDC6F9436742D806A174D6889BA686A62D4996392DEFB228FE4A5D156D7EE0A7089AE6B5EB29774E7644E68794602E4D721450909E38BDA3BF34AA409316CC7BD7C384F6BAD9C45A56E95033181A86FC1E259E9EFAAF09FBC7388CA53FB03EDA8004F84499E965A68831C48079DEB3D8A4A3644DC52C1D786FBB09A4A2EF6833BF68E5EED439CE4D07BEF249EC761B170880B7162157B02E0C85390CF31A30AD8A083FDB46F20BD82491B60FAB87F446F0CDD4771323A40FA8479BAD6A682C93EF7E3E8CA53C16A07440DDF6CFDEA7403BF6BED1CA89FA715A71BADA8F0A50C202703CA2999108F7EFABFD517D85D8D542B0BE9EEAB0CC33DF24D389A50C8C11CF0868DC71FA30DD86F86455D7D890F8823DA17A44FE991D73BC39FFD751530390708B46EB9705CFD81306056DDB905A157C0F9ABD737E794053A51B19AB6C23D9D3E66F86C7F62156F657C8AFAC277DAF510193EDB0F5EA968EA73B0CE3D58182F58516B78867FDE2D3FCC5777451CCCC2E52C985CB3249827CB55904C6E97AB55310FE3F0F6D7E80178C3F5EFDFAB3C858BB5B0021E097328F650E2E3D997E1D166A0DFCF28D01E739FC7D3F063128541711D46C1644A67C16C7A9D044512C5ABE964799714C9887BF2CA67222451343C389E7CB2705C32C1D551ABA342632F8804DBBF14418E4A90F39F41FE1B0000FFFF0300504B0304140006000800000021006C40BF2A30020000C405000018000000786C2F776F726B7368656574732F7368656574312E786D6C9C94DB6E9C301086EF2BF51D2CDF2FA73DA44140A40445CD45A5AA697BEF3503588B31B5BD87A8EABB770C858DB4598906016B9BE1FB673CFF92DC9D64430EA08D506D4A432FA0045AAE0AD15629FDF1FD71F1891263595BB046B590D21730F42EFBF821392ABD3335802548684D4A6B6BBBD8F70DAF4132E3A90E5A7C522A2D99C5A9AE7CD3696045FF926CFC280836BE64A2A50321D67318AA2C05875CF1BD84D60E100D0DB398BFA94567469AE4737092E9DDBE5B70253B446C4523EC4B0FA544F2F8A96A9566DB06EB3E852BC6C949E319E1B51C65FAF50B2529B8564695D643B23FE47C59FEAD7FEB333E912EEB9F850957BE8683700D3CA3A2F7A514AE275674862DDF09DB4C30B75D3ADE8B22A5BF837FC7027F43770BCEB7F1D91F9A2585C00EBBAA888632A5F7619C6FA89F25BD7F7E0A389A576362D9F6191AE0165023A4C4D973ABD4CE053EE1528044D3073822E3561CE0019A26A5F90D3AFC57AF814314F02785D7E351EDB137F4574D0A28D9BEB1DFD4F13388AAB628BBF2D66BACD459252E5E72301C3D8ADADE724A3C67966589564782EDC63C4DC7DC9F278A57575ECC12EE421F422CE09085897FC0AC385EC89840D8ACB9A0FBA807451368C00FAB57F0D8BED9F8658F5FBE9D2716391794632CEE9DE971C1DB38DCECD9388C9D7057CADCFC070E6327DC792F87A60C061A3ADDB10ABE305D89D69006CADE0D68383D3826F0706C55E73C7283196E95B54A8EB31ABF9680BD77FE21A552769C38934EDFDFEC2F000000FFFF0300504B0304140006000800000021006F8D3DFF420100005102000011000801646F6350726F70732F636F72652E786D6C20A2040128A00001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007C92514BC3301485DF05FF43C97B9BA4657386B603953D39109C28BE85E46E2B366948A2DDFEBD69BBD50E868FF79E93EF9E7B49BE3CA83AFA01EBAA461788260445A045232BBD2BD0DB66152F50E43CD792D78D86021DC1A165797B930BC34463E1C53606ACAFC04581A41D13A6407BEF0DC3D8893D28EE92E0D041DC3656711F4ABBC3868B2FBE039C1232C70A3C97DC73DC01633312D10929C58834DFB6EE015260A84181F60ED384E23FAF07ABDCD507BD3271AACA1F4DD8E91477CA96621047F7C155A3B16DDBA4CDFA18213FC51FEBE7D77ED5B8D2DDAD04A0329782090BDC37B6CCF1B40887ABB9F3EB70E36D05F2E118F42B3D29FAB80304641402B021EE5979CF1E9F362B54A684CE62328FC96C43178CDEB1947C76232FDE778186863A0DFE9F781F932CCEE88610364B59369F10CF8021F7E527287F010000FFFF0300504B03041400060008000000210061490910890100001103000010000801646F6350726F70732F6170702E786D6C20A2040128A00001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009C92416FDB300C85EF03FA1F0CDD1B39DD500C81AC624857F4B0610192B6674DA663A1B22488AC91ECD78FB6D1D4D97AEA8DE47B78FA4449DD1C3A5FF490D1C55089E5A21405041B6B17F69578D8DD5D7E15059209B5F13140258E80E2465F7C529B1C13647280054704AC444B945652A26DA133B86039B0D2C4DC19E236EF656C1A67E136DA970E02C9ABB2BC9670200835D497E91428A6C4554F1F0DADA31DF8F071774C0CACD5B794BCB386F896FAA7B339626CA8F87EB0E0959C8B8AE9B6605FB2A3A32E959CB76A6B8D873507EBC6780425DF06EA1ECCB0B48D7119B5EA69D583A5980B747F786D57A2F86D10069C4AF4263B1388B106DBD48CB54F48593FC5FC8C2D00A1926C98866339F7CE6BF7452F470317E7C621600261E11C71E7C803FE6A3626D33BC4CB39F1C830F14E38DB816F3A73CE375E994FFA277B1DBB64C2918553F5C385677C48BB786B085ED7793E54DBD664A8F9054EEB3E0DD43D6F32FB2164DD9AB087FAD5F3BF303CFEE3F4C3F5F27A517E2EF95D673325DFFEB2FE0B0000FFFF0300504B01022D001400060008000000210062EE9D685E010000900400001300000000000000000000000000000000005B436F6E74656E745F54797065735D2E786D6C504B01022D0014000600080000002100B5553023F40000004C0200000B00000000000000000000000000970300005F72656C732F2E72656C73504B01022D0014000600080000002100813E9497F3000000BA0200001A00000000000000000000000000BC060000786C2F5F72656C732F776F726B626F6F6B2E786D6C2E72656C73504B01022D0014000600080000002100779BFDB086020000AF0500000F00000000000000000000000000EF080000786C2F776F726B626F6F6B2E786D6C504B01022D0014000600080000002100053CDBAAA2000000D30000001400000000000000000000000000A20B0000786C2F736861726564537472696E67732E786D6C504B01022D0014000600080000002100753E9969930600008C1A00001300000000000000000000000000760C0000786C2F7468656D652F7468656D65312E786D6C504B01022D001400060008000000210079A1806CA4020000520600000D000000000000000000000000003A130000786C2F7374796C65732E786D6C504B01022D00140006000800000021006C40BF2A30020000C4050000180000000000000000000000000009160000786C2F776F726B7368656574732F7368656574312E786D6C504B01022D00140006000800000021006F8D3DFF420100005102000011000000000000000000000000006F180000646F6350726F70732F636F72652E786D6C504B01022D00140006000800000021006149091089010000110300001000000000000000000000000000E81A0000646F6350726F70732F6170702E786D6C504B0506000000000A000A0080020000A71D00000000"



