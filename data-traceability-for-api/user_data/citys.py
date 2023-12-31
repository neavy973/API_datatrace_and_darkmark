from random import randint
def city(x):
  citys=[
  {
    "name": "北京",
    "name_en": "beijing",
    "city": [
      {
        "name": "北京",
        "county": [
          {
            "name": "北京",
            "code": "CN101010100",
            "name_en": "beijing"
          },
          {
            "name": "海淀",
            "code": "CN101010200",
            "name_en": "haidian"
          },
          {
            "name": "朝阳",
            "code": "CN101010300",
            "name_en": "chaoyang"
          },
          {
            "name": "顺义",
            "code": "CN101010400",
            "name_en": "shunyi"
          },
          {
            "name": "怀柔",
            "code": "CN101010500",
            "name_en": "huairou"
          },
          {
            "name": "通州",
            "code": "CN101010600",
            "name_en": "tongzhou"
          },
          {
            "name": "昌平",
            "code": "CN101010700",
            "name_en": "changping"
          },
          {
            "name": "延庆",
            "code": "CN101010800",
            "name_en": "yanqing"
          },
          {
            "name": "丰台",
            "code": "CN101010900",
            "name_en": "fengtai"
          },
          {
            "name": "石景山",
            "code": "CN101011000",
            "name_en": "shijingshan"
          },
          {
            "name": "大兴",
            "code": "CN101011100",
            "name_en": "daxing"
          },
          {
            "name": "房山",
            "code": "CN101011200",
            "name_en": "fangshan"
          },
          {
            "name": "密云",
            "code": "CN101011300",
            "name_en": "miyun"
          },
          {
            "name": "门头沟",
            "code": "CN101011400",
            "name_en": "mentougou"
          },
          {
            "name": "平谷",
            "code": "CN101011500",
            "name_en": "pinggu"
          }
        ]
      }
    ]
  },
  {
    "name": "上海",
    "name_en": "shanghai",
    "city": [
      {
        "name": "上海",
        "county": [
          {
            "name": "上海",
            "code": "CN101020100",
            "name_en": "shanghai"
          },
          {
            "name": "闵行",
            "code": "CN101020200",
            "name_en": "minhang"
          },
          {
            "name": "宝山",
            "code": "CN101020300",
            "name_en": "baoshan"
          },
          {
            "name": "嘉定",
            "code": "CN101020500",
            "name_en": "jiading"
          },
          {
            "name": "浦东南汇",
            "code": "CN101020600",
            "name_en": "nanhui"
          },
          {
            "name": "金山",
            "code": "CN101020700",
            "name_en": "jinshan"
          },
          {
            "name": "青浦",
            "code": "CN101020800",
            "name_en": "qingpu"
          },
          {
            "name": "松江",
            "code": "CN101020900",
            "name_en": "songjiang"
          },
          {
            "name": "奉贤",
            "code": "CN101021000",
            "name_en": "fengxian"
          },
          {
            "name": "崇明",
            "code": "CN101021100",
            "name_en": "chongming"
          },
          {
            "name": "徐家汇",
            "code": "CN101021200",
            "name_en": "xujiahui"
          },
          {
            "name": "浦东",
            "code": "CN101021300",
            "name_en": "pudong"
          }
        ]
      }
    ]
  },
  {
    "name": "天津",
    "name_en": "tianjin",
    "city": [
      {
        "name": "天津",
        "county": [
          {
            "name": "天津",
            "code": "CN101030100",
            "name_en": "tianjin"
          },
          {
            "name": "武清",
            "code": "CN101030200",
            "name_en": "wuqing"
          },
          {
            "name": "宝坻",
            "code": "CN101030300",
            "name_en": "baodi"
          },
          {
            "name": "东丽",
            "code": "CN101030400",
            "name_en": "dongli"
          },
          {
            "name": "西青",
            "code": "CN101030500",
            "name_en": "xiqing"
          },
          {
            "name": "北辰",
            "code": "CN101030600",
            "name_en": "beichen"
          },
          {
            "name": "宁河",
            "code": "CN101030700",
            "name_en": "ninghe"
          },
          {
            "name": "汉沽",
            "code": "CN101030800",
            "name_en": "hangu"
          },
          {
            "name": "静海",
            "code": "CN101030900",
            "name_en": "jinghai"
          },
          {
            "name": "津南",
            "code": "CN101031000",
            "name_en": "jinnan"
          },
          {
            "name": "塘沽",
            "code": "CN101031100",
            "name_en": "tanggu"
          },
          {
            "name": "大港",
            "code": "CN101031200",
            "name_en": "dagang"
          },
          {
            "name": "蓟县",
            "code": "CN101031400",
            "name_en": "jixian"
          }
        ]
      }
    ]
  },
  {
    "name": "重庆",
    "name_en": "chongqing",
    "city": [
      {
        "name": "重庆",
        "county": [
          {
            "name": "重庆",
            "code": "CN101040100",
            "name_en": "chongqing"
          },
          {
            "name": "永川",
            "code": "CN101040200",
            "name_en": "yongchuan"
          },
          {
            "name": "合川",
            "code": "CN101040300",
            "name_en": "hechuan"
          },
          {
            "name": "南川",
            "code": "CN101040400",
            "name_en": "nanchuan"
          },
          {
            "name": "江津",
            "code": "CN101040500",
            "name_en": "jiangjin"
          },
          {
            "name": "万盛",
            "code": "CN101040600",
            "name_en": "wansheng"
          },
          {
            "name": "渝北",
            "code": "CN101040700",
            "name_en": "yubei"
          },
          {
            "name": "北碚",
            "code": "CN101040800",
            "name_en": "beibei"
          },
          {
            "name": "巴南",
            "code": "CN101040900",
            "name_en": "banan"
          },
          {
            "name": "长寿",
            "code": "CN101041000",
            "name_en": "changshou"
          },
          {
            "name": "黔江",
            "code": "CN101041100",
            "name_en": "qianjiang"
          },
          {
            "name": "万州",
            "code": "CN101041300",
            "name_en": "wanzhou"
          },
          {
            "name": "涪陵",
            "code": "CN101041400",
            "name_en": "fuling"
          },
          {
            "name": "开县",
            "code": "CN101041500",
            "name_en": "kaixian"
          },
          {
            "name": "城口",
            "code": "CN101041600",
            "name_en": "chengkou"
          },
          {
            "name": "云阳",
            "code": "CN101041700",
            "name_en": "yunyang"
          },
          {
            "name": "巫溪",
            "code": "CN101041800",
            "name_en": "wuxi"
          },
          {
            "name": "奉节",
            "code": "CN101041900",
            "name_en": "fengjie"
          },
          {
            "name": "巫山",
            "code": "CN101042000",
            "name_en": "wushan"
          },
          {
            "name": "潼南",
            "code": "CN101042100",
            "name_en": "tongnan"
          },
          {
            "name": "垫江",
            "code": "CN101042200",
            "name_en": "dianjiang"
          },
          {
            "name": "梁平",
            "code": "CN101042300",
            "name_en": "liangping"
          },
          {
            "name": "忠县",
            "code": "CN101042400",
            "name_en": "zhongxian"
          },
          {
            "name": "石柱",
            "code": "CN101042500",
            "name_en": "shizhu"
          },
          {
            "name": "大足",
            "code": "CN101042600",
            "name_en": "dazu"
          },
          {
            "name": "荣昌",
            "code": "CN101042700",
            "name_en": "rongchang"
          },
          {
            "name": "铜梁",
            "code": "CN101042800",
            "name_en": "tongliang"
          },
          {
            "name": "璧山",
            "code": "CN101042900",
            "name_en": "bishan"
          },
          {
            "name": "丰都",
            "code": "CN101043000",
            "name_en": "fengdu"
          },
          {
            "name": "武隆",
            "code": "CN101043100",
            "name_en": "wulong"
          },
          {
            "name": "彭水",
            "code": "CN101043200",
            "name_en": "pengshui"
          },
          {
            "name": "綦江",
            "code": "CN101043300",
            "name_en": "qijiang"
          },
          {
            "name": "酉阳",
            "code": "CN101043400",
            "name_en": "youyang"
          },
          {
            "name": "秀山",
            "code": "CN101043600",
            "name_en": "xiushan"
          }
        ]
      }
    ]
  },
  {
    "name": "黑龙江",
    "name_en": "heilongjiang",
    "city": [
      {
        "name": "哈尔滨",
        "county": [
          {
            "name": "哈尔滨",
            "code": "CN101050101",
            "name_en": "haerbin"
          },
          {
            "name": "双城",
            "code": "CN101050102",
            "name_en": "shuangcheng"
          },
          {
            "name": "呼兰",
            "code": "CN101050103",
            "name_en": "hulan"
          },
          {
            "name": "阿城",
            "code": "CN101050104",
            "name_en": "acheng"
          },
          {
            "name": "宾县",
            "code": "CN101050105",
            "name_en": "binxian"
          },
          {
            "name": "依兰",
            "code": "CN101050106",
            "name_en": "yilan"
          },
          {
            "name": "巴彦",
            "code": "CN101050107",
            "name_en": "bayan"
          },
          {
            "name": "通河",
            "code": "CN101050108",
            "name_en": "tonghe"
          },
          {
            "name": "方正",
            "code": "CN101050109",
            "name_en": "fangzheng"
          },
          {
            "name": "延寿",
            "code": "CN101050110",
            "name_en": "yanshou"
          },
          {
            "name": "尚志",
            "code": "CN101050111",
            "name_en": "shangzhi"
          },
          {
            "name": "五常",
            "code": "CN101050112",
            "name_en": "wuchang"
          },
          {
            "name": "木兰",
            "code": "CN101050113",
            "name_en": "mulan"
          }
        ]
      },
      {
        "name": "齐齐哈尔",
        "county": [
          {
            "name": "齐齐哈尔",
            "code": "CN101050201",
            "name_en": "qiqihaer"
          },
          {
            "name": "讷河",
            "code": "CN101050202",
            "name_en": "nehe"
          },
          {
            "name": "龙江",
            "code": "CN101050203",
            "name_en": "longjiang"
          },
          {
            "name": "甘南",
            "code": "CN101050204",
            "name_en": "gannan"
          },
          {
            "name": "富裕",
            "code": "CN101050205",
            "name_en": "fuyu"
          },
          {
            "name": "依安",
            "code": "CN101050206",
            "name_en": "yian"
          },
          {
            "name": "拜泉",
            "code": "CN101050207",
            "name_en": "baiquan"
          },
          {
            "name": "克山",
            "code": "CN101050208",
            "name_en": "keshan"
          },
          {
            "name": "克东",
            "code": "CN101050209",
            "name_en": "kedong"
          },
          {
            "name": "泰来",
            "code": "CN101050210",
            "name_en": "tailai"
          }
        ]
      },
      {
        "name": "牡丹江",
        "county": [
          {
            "name": "牡丹江",
            "code": "CN101050301",
            "name_en": "mudanjiang"
          },
          {
            "name": "海林",
            "code": "CN101050302",
            "name_en": "hailin"
          },
          {
            "name": "穆棱",
            "code": "CN101050303",
            "name_en": "muling"
          },
          {
            "name": "林口",
            "code": "CN101050304",
            "name_en": "linkou"
          },
          {
            "name": "绥芬河",
            "code": "CN101050305",
            "name_en": "suifenhe"
          },
          {
            "name": "宁安",
            "code": "CN101050306",
            "name_en": "ningan"
          },
          {
            "name": "东宁",
            "code": "CN101050307",
            "name_en": "dongning"
          }
        ]
      },
      {
        "name": "佳木斯",
        "county": [
          {
            "name": "佳木斯",
            "code": "CN101050401",
            "name_en": "jiamusi"
          },
          {
            "name": "汤原",
            "code": "CN101050402",
            "name_en": "tangyuan"
          },
          {
            "name": "抚远",
            "code": "CN101050403",
            "name_en": "fuyuan"
          },
          {
            "name": "桦川",
            "code": "CN101050404",
            "name_en": "huachuan"
          },
          {
            "name": "桦南",
            "code": "CN101050405",
            "name_en": "huanan"
          },
          {
            "name": "同江",
            "code": "CN101050406",
            "name_en": "tongjiang"
          },
          {
            "name": "富锦",
            "code": "CN101050407",
            "name_en": "fujin"
          }
        ]
      },
      {
        "name": "绥化",
        "county": [
          {
            "name": "绥化",
            "code": "CN101050501",
            "name_en": "suihua"
          },
          {
            "name": "肇东",
            "code": "CN101050502",
            "name_en": "zhaodong"
          },
          {
            "name": "安达",
            "code": "CN101050503",
            "name_en": "anda"
          },
          {
            "name": "海伦",
            "code": "CN101050504",
            "name_en": "hailun"
          },
          {
            "name": "明水",
            "code": "CN101050505",
            "name_en": "mingshui"
          },
          {
            "name": "望奎",
            "code": "CN101050506",
            "name_en": "wangkui"
          },
          {
            "name": "兰西",
            "code": "CN101050507",
            "name_en": "lanxi"
          },
          {
            "name": "青冈",
            "code": "CN101050508",
            "name_en": "qinggang"
          },
          {
            "name": "庆安",
            "code": "CN101050509",
            "name_en": "qingan"
          },
          {
            "name": "绥棱",
            "code": "CN101050510",
            "name_en": "suiling"
          }
        ]
      },
      {
        "name": "黑河",
        "county": [
          {
            "name": "黑河",
            "code": "CN101050601",
            "name_en": "heihe"
          },
          {
            "name": "嫩江",
            "code": "CN101050602",
            "name_en": "nenjiang"
          },
          {
            "name": "孙吴",
            "code": "CN101050603",
            "name_en": "sunwu"
          },
          {
            "name": "逊克",
            "code": "CN101050604",
            "name_en": "xunke"
          },
          {
            "name": "五大连池",
            "code": "CN101050605",
            "name_en": "wudalianchi"
          },
          {
            "name": "北安",
            "code": "CN101050606",
            "name_en": "beian"
          }
        ]
      },
      {
        "name": "大兴安岭",
        "county": [
          {
            "name": "大兴安岭",
            "code": "CN101050701",
            "name_en": "daxinganling"
          },
          {
            "name": "塔河",
            "code": "CN101050702",
            "name_en": "tahe"
          },
          {
            "name": "漠河",
            "code": "CN101050703",
            "name_en": "mohe"
          },
          {
            "name": "呼玛",
            "code": "CN101050704",
            "name_en": "huma"
          },
          {
            "name": "呼中",
            "code": "CN101050705",
            "name_en": "huzhong"
          },
          {
            "name": "新林",
            "code": "CN101050706",
            "name_en": "xinlin"
          },
          {
            "name": "加格达奇",
            "code": "CN101050708",
            "name_en": "jiagedaqi"
          }
        ]
      },
      {
        "name": "伊春",
        "county": [
          {
            "name": "伊春",
            "code": "CN101050801",
            "name_en": "yichun"
          },
          {
            "name": "乌伊岭",
            "code": "CN101050802",
            "name_en": "wuyiling"
          },
          {
            "name": "五营",
            "code": "CN101050803",
            "name_en": "wuying"
          },
          {
            "name": "铁力",
            "code": "CN101050804",
            "name_en": "tieli"
          },
          {
            "name": "嘉荫",
            "code": "CN101050805",
            "name_en": "jiayin"
          }
        ]
      },
      {
        "name": "大庆",
        "county": [
          {
            "name": "大庆",
            "code": "CN101050901",
            "name_en": "daqing"
          },
          {
            "name": "林甸",
            "code": "CN101050902",
            "name_en": "lindian"
          },
          {
            "name": "肇州",
            "code": "CN101050903",
            "name_en": "zhaozhou"
          },
          {
            "name": "肇源",
            "code": "CN101050904",
            "name_en": "zhaoyuan"
          },
          {
            "name": "杜尔伯特",
            "code": "CN101050905",
            "name_en": "duerbote"
          }
        ]
      },
      {
        "name": "七台河",
        "county": [
          {
            "name": "七台河",
            "code": "CN101051002",
            "name_en": "qitaihe"
          },
          {
            "name": "勃利",
            "code": "CN101051003",
            "name_en": "boli"
          }
        ]
      },
      {
        "name": "鸡西",
        "county": [
          {
            "name": "鸡西",
            "code": "CN101051101",
            "name_en": "jixi"
          },
          {
            "name": "虎林",
            "code": "CN101051102",
            "name_en": "hulin"
          },
          {
            "name": "密山",
            "code": "CN101051103",
            "name_en": "mishan"
          },
          {
            "name": "鸡东",
            "code": "CN101051104",
            "name_en": "jidong"
          }
        ]
      },
      {
        "name": "鹤岗",
        "county": [
          {
            "name": "鹤岗",
            "code": "CN101051201",
            "name_en": "hegang"
          },
          {
            "name": "绥滨",
            "code": "CN101051202",
            "name_en": "suibin"
          },
          {
            "name": "萝北",
            "code": "CN101051203",
            "name_en": "luobei"
          }
        ]
      },
      {
        "name": "双鸭山",
        "county": [
          {
            "name": "双鸭山",
            "code": "CN101051301",
            "name_en": "shuangyashan"
          },
          {
            "name": "集贤",
            "code": "CN101051302",
            "name_en": "jixian"
          },
          {
            "name": "宝清",
            "code": "CN101051303",
            "name_en": "baoqing"
          },
          {
            "name": "饶河",
            "code": "CN101051304",
            "name_en": "raohe"
          },
          {
            "name": "友谊",
            "code": "CN101051305",
            "name_en": "youyi"
          }
        ]
      }
    ]
  },
  {
    "name": "吉林",
    "name_en": "jilin",
    "city": [
      {
        "name": "长春",
        "county": [
          {
            "name": "长春",
            "code": "CN101060101",
            "name_en": "changchun"
          },
          {
            "name": "农安",
            "code": "CN101060102",
            "name_en": "nongan"
          },
          {
            "name": "德惠",
            "code": "CN101060103",
            "name_en": "dehui"
          },
          {
            "name": "九台",
            "code": "CN101060104",
            "name_en": "jiutai"
          },
          {
            "name": "榆树",
            "code": "CN101060105",
            "name_en": "yushu"
          },
          {
            "name": "双阳",
            "code": "CN101060106",
            "name_en": "shuangyang"
          }
        ]
      },
      {
        "name": "吉林",
        "county": [
          {
            "name": "吉林",
            "code": "CN101060201",
            "name_en": "jilin"
          },
          {
            "name": "舒兰",
            "code": "CN101060202",
            "name_en": "shulan"
          },
          {
            "name": "永吉",
            "code": "CN101060203",
            "name_en": "yongji"
          },
          {
            "name": "蛟河",
            "code": "CN101060204",
            "name_en": "jiaohe"
          },
          {
            "name": "磐石",
            "code": "CN101060205",
            "name_en": "panshi"
          },
          {
            "name": "桦甸",
            "code": "CN101060206",
            "name_en": "huadian"
          }
        ]
      },
      {
        "name": "延边",
        "county": [
          {
            "name": "延吉",
            "code": "CN101060301",
            "name_en": "yanji"
          },
          {
            "name": "敦化",
            "code": "CN101060302",
            "name_en": "dunhua"
          },
          {
            "name": "安图",
            "code": "CN101060303",
            "name_en": "antu"
          },
          {
            "name": "汪清",
            "code": "CN101060304",
            "name_en": "wangqing"
          },
          {
            "name": "和龙",
            "code": "CN101060305",
            "name_en": "helong"
          },
          {
            "name": "龙井",
            "code": "CN101060307",
            "name_en": "longjing"
          },
          {
            "name": "珲春",
            "code": "CN101060308",
            "name_en": "hunchun"
          },
          {
            "name": "图们",
            "code": "CN101060309",
            "name_en": "tumen"
          }
        ]
      },
      {
        "name": "四平",
        "county": [
          {
            "name": "四平",
            "code": "CN101060401",
            "name_en": "siping"
          },
          {
            "name": "双辽",
            "code": "CN101060402",
            "name_en": "shuangliao"
          },
          {
            "name": "梨树",
            "code": "CN101060403",
            "name_en": "lishu"
          },
          {
            "name": "公主岭",
            "code": "CN101060404",
            "name_en": "gongzhuling"
          },
          {
            "name": "伊通",
            "code": "CN101060405",
            "name_en": "yitong"
          }
        ]
      },
      {
        "name": "通化",
        "county": [
          {
            "name": "通化",
            "code": "CN101060501",
            "name_en": "tonghua"
          },
          {
            "name": "梅河口",
            "code": "CN101060502",
            "name_en": "meihekou"
          },
          {
            "name": "柳河",
            "code": "CN101060503",
            "name_en": "liuhe"
          },
          {
            "name": "辉南",
            "code": "CN101060504",
            "name_en": "huinan"
          },
          {
            "name": "集安",
            "code": "CN101060505",
            "name_en": "jian"
          },
          {
            "name": "通化县",
            "code": "CN101060506",
            "name_en": "tonghuaxian"
          }
        ]
      },
      {
        "name": "白城",
        "county": [
          {
            "name": "白城",
            "code": "CN101060601",
            "name_en": "baicheng"
          },
          {
            "name": "洮南",
            "code": "CN101060602",
            "name_en": "taonan"
          },
          {
            "name": "大安",
            "code": "CN101060603",
            "name_en": "daan"
          },
          {
            "name": "镇赉",
            "code": "CN101060604",
            "name_en": "zhenlai"
          },
          {
            "name": "通榆",
            "code": "CN101060605",
            "name_en": "tongyu"
          }
        ]
      },
      {
        "name": "辽源",
        "county": [
          {
            "name": "辽源",
            "code": "CN101060701",
            "name_en": "liaoyuan"
          },
          {
            "name": "东丰",
            "code": "CN101060702",
            "name_en": "dongfeng"
          },
          {
            "name": "东辽",
            "code": "CN101060703",
            "name_en": "dongliao"
          }
        ]
      },
      {
        "name": "松原",
        "county": [
          {
            "name": "松原",
            "code": "CN101060801",
            "name_en": "songyuan"
          },
          {
            "name": "乾安",
            "code": "CN101060802",
            "name_en": "qianan"
          },
          {
            "name": "前郭",
            "code": "CN101060803",
            "name_en": "qianguo"
          },
          {
            "name": "长岭",
            "code": "CN101060804",
            "name_en": "changling"
          },
          {
            "name": "扶余",
            "code": "CN101060805",
            "name_en": "fuyu"
          }
        ]
      },
      {
        "name": "白山",
        "county": [
          {
            "name": "白山",
            "code": "CN101060901",
            "name_en": "baishan"
          },
          {
            "name": "靖宇",
            "code": "CN101060902",
            "name_en": "jingyu"
          },
          {
            "name": "临江",
            "code": "CN101060903",
            "name_en": "linjiang"
          },
          {
            "name": "东岗",
            "code": "CN101060904",
            "name_en": "donggang"
          },
          {
            "name": "长白",
            "code": "CN101060905",
            "name_en": "changbai"
          },
          {
            "name": "抚松",
            "code": "CN101060906",
            "name_en": "fusong"
          },
          {
            "name": "江源",
            "code": "CN101060907",
            "name_en": "jiangyuan"
          }
        ]
      }
    ]
  },
  {
    "name": "辽宁",
    "name_en": "liaoning",
    "city": [
      {
        "name": "沈阳",
        "county": [
          {
            "name": "沈阳",
            "code": "CN101070101",
            "name_en": "shenyang"
          },
          {
            "name": "辽中",
            "code": "CN101070103",
            "name_en": "liaozhong"
          },
          {
            "name": "康平",
            "code": "CN101070104",
            "name_en": "kangping"
          },
          {
            "name": "法库",
            "code": "CN101070105",
            "name_en": "faku"
          },
          {
            "name": "新民",
            "code": "CN101070106",
            "name_en": "xinmin"
          }
        ]
      },
      {
        "name": "大连",
        "county": [
          {
            "name": "大连",
            "code": "CN101070201",
            "name_en": "dalian"
          },
          {
            "name": "瓦房店",
            "code": "CN101070202",
            "name_en": "wafangdian"
          },
          {
            "name": "金州",
            "code": "CN101070203",
            "name_en": "jinzhou"
          },
          {
            "name": "普兰店",
            "code": "CN101070204",
            "name_en": "pulandian"
          },
          {
            "name": "旅顺",
            "code": "CN101070205",
            "name_en": "lvshun"
          },
          {
            "name": "长海",
            "code": "CN101070206",
            "name_en": "changhai"
          },
          {
            "name": "庄河",
            "code": "CN101070207",
            "name_en": "zhuanghe"
          }
        ]
      },
      {
        "name": "鞍山",
        "county": [
          {
            "name": "鞍山",
            "code": "CN101070301",
            "name_en": "anshan"
          },
          {
            "name": "台安",
            "code": "CN101070302",
            "name_en": "taian"
          },
          {
            "name": "岫岩",
            "code": "CN101070303",
            "name_en": "xiuyan"
          },
          {
            "name": "海城",
            "code": "CN101070304",
            "name_en": "haicheng"
          }
        ]
      },
      {
        "name": "抚顺",
        "county": [
          {
            "name": "抚顺",
            "code": "CN101070401",
            "name_en": "fushun"
          },
          {
            "name": "新宾",
            "code": "CN101070402",
            "name_en": "xinbin"
          },
          {
            "name": "清原",
            "code": "CN101070403",
            "name_en": "qingyuan"
          },
          {
            "name": "章党",
            "code": "CN101070404",
            "name_en": "zhangdang"
          }
        ]
      },
      {
        "name": "本溪",
        "county": [
          {
            "name": "本溪",
            "code": "CN101070501",
            "name_en": "benxi"
          },
          {
            "name": "本溪县",
            "code": "CN101070502",
            "name_en": "benxixian"
          },
          {
            "name": "桓仁",
            "code": "CN101070504",
            "name_en": "huanren"
          }
        ]
      },
      {
        "name": "丹东",
        "county": [
          {
            "name": "丹东",
            "code": "CN101070601",
            "name_en": "dandong"
          },
          {
            "name": "凤城",
            "code": "CN101070602",
            "name_en": "fengcheng"
          },
          {
            "name": "宽甸",
            "code": "CN101070603",
            "name_en": "kuandian"
          },
          {
            "name": "东港",
            "code": "CN101070604",
            "name_en": "donggang"
          }
        ]
      },
      {
        "name": "锦州",
        "county": [
          {
            "name": "锦州",
            "code": "CN101070701",
            "name_en": "jinzhou"
          },
          {
            "name": "凌海",
            "code": "CN101070702",
            "name_en": "linghai"
          },
          {
            "name": "义县",
            "code": "CN101070704",
            "name_en": "yixian"
          },
          {
            "name": "黑山",
            "code": "CN101070705",
            "name_en": "heishan"
          },
          {
            "name": "北镇",
            "code": "CN101070706",
            "name_en": "beizhen"
          }
        ]
      },
      {
        "name": "营口",
        "county": [
          {
            "name": "营口",
            "code": "CN101070801",
            "name_en": "yingkou"
          },
          {
            "name": "大石桥",
            "code": "CN101070802",
            "name_en": "dashiqiao"
          },
          {
            "name": "盖州",
            "code": "CN101070803",
            "name_en": "gaizhou"
          }
        ]
      },
      {
        "name": "阜新",
        "county": [
          {
            "name": "阜新",
            "code": "CN101070901",
            "name_en": "fuxin"
          },
          {
            "name": "彰武",
            "code": "CN101070902",
            "name_en": "zhangwu"
          }
        ]
      },
      {
        "name": "辽阳",
        "county": [
          {
            "name": "辽阳",
            "code": "CN101071001",
            "name_en": "liaoyang"
          },
          {
            "name": "辽阳县",
            "code": "CN101071002",
            "name_en": "liaoyangxian"
          },
          {
            "name": "灯塔",
            "code": "CN101071003",
            "name_en": "dengta"
          },
          {
            "name": "弓长岭",
            "code": "CN101071004",
            "name_en": "gongchangling"
          }
        ]
      },
      {
        "name": "铁岭",
        "county": [
          {
            "name": "铁岭",
            "code": "CN101071101",
            "name_en": "tieling"
          },
          {
            "name": "开原",
            "code": "CN101071102",
            "name_en": "kaiyuan"
          },
          {
            "name": "昌图",
            "code": "CN101071103",
            "name_en": "changtu"
          },
          {
            "name": "西丰",
            "code": "CN101071104",
            "name_en": "xifeng"
          },
          {
            "name": "调兵山",
            "code": "CN101071105",
            "name_en": "tiefa"
          }
        ]
      },
      {
        "name": "朝阳",
        "county": [
          {
            "name": "朝阳",
            "code": "CN101071201",
            "name_en": "chaoyang"
          },
          {
            "name": "凌源",
            "code": "CN101071203",
            "name_en": "lingyuan"
          },
          {
            "name": "喀左",
            "code": "CN101071204",
            "name_en": "kazuo"
          },
          {
            "name": "北票",
            "code": "CN101071205",
            "name_en": "beipiao"
          },
          {
            "name": "建平县",
            "code": "CN101071207",
            "name_en": "jianpingxian"
          }
        ]
      },
      {
        "name": "盘锦",
        "county": [
          {
            "name": "盘锦",
            "code": "CN101071301",
            "name_en": "panjin"
          },
          {
            "name": "大洼",
            "code": "CN101071302",
            "name_en": "dawa"
          },
          {
            "name": "盘山",
            "code": "CN101071303",
            "name_en": "panshan"
          }
        ]
      },
      {
        "name": "葫芦岛",
        "county": [
          {
            "name": "葫芦岛",
            "code": "CN101071401",
            "name_en": "huludao"
          },
          {
            "name": "建昌",
            "code": "CN101071402",
            "name_en": "jianchang"
          },
          {
            "name": "绥中",
            "code": "CN101071403",
            "name_en": "suizhong"
          },
          {
            "name": "兴城",
            "code": "CN101071404",
            "name_en": "xingcheng"
          }
        ]
      }
    ]
  },
  {
    "name": "内蒙古",
    "name_en": "neimenggu",
    "city": [
      {
        "name": "呼和浩特",
        "county": [
          {
            "name": "呼和浩特",
            "code": "CN101080101",
            "name_en": "huhehaote"
          },
          {
            "name": "土左旗",
            "code": "CN101080102",
            "name_en": "tuzuoqi"
          },
          {
            "name": "托县",
            "code": "CN101080103",
            "name_en": "tuoxian"
          },
          {
            "name": "和林",
            "code": "CN101080104",
            "name_en": "helin"
          },
          {
            "name": "清水河",
            "code": "CN101080105",
            "name_en": "qingshuihe"
          },
          {
            "name": "呼市郊区",
            "code": "CN101080106",
            "name_en": "hushijiaoqu"
          },
          {
            "name": "武川",
            "code": "CN101080107",
            "name_en": "wuchuan"
          }
        ]
      },
      {
        "name": "包头",
        "county": [
          {
            "name": "包头",
            "code": "CN101080201",
            "name_en": "baotou"
          },
          {
            "name": "白云鄂博",
            "code": "CN101080202",
            "name_en": "baiyunebo"
          },
          {
            "name": "满都拉",
            "code": "CN101080203",
            "name_en": "mandula"
          },
          {
            "name": "土右旗",
            "code": "CN101080204",
            "name_en": "tuyouqi"
          },
          {
            "name": "固阳",
            "code": "CN101080205",
            "name_en": "guyang"
          },
          {
            "name": "达茂旗",
            "code": "CN101080206",
            "name_en": "damaoqi"
          },
          {
            "name": "希拉穆仁",
            "code": "CN101080207",
            "name_en": "xilamuren"
          }
        ]
      },
      {
        "name": "乌海",
        "county": [
          {
            "name": "乌海",
            "code": "CN101080301",
            "name_en": "wuhai"
          }
        ]
      },
      {
        "name": "乌兰察布",
        "county": [
          {
            "name": "集宁",
            "code": "CN101080401",
            "name_en": "jining"
          },
          {
            "name": "卓资",
            "code": "CN101080402",
            "name_en": "zhuozi"
          },
          {
            "name": "化德",
            "code": "CN101080403",
            "name_en": "huade"
          },
          {
            "name": "商都",
            "code": "CN101080404",
            "name_en": "shangdu"
          },
          {
            "name": "兴和",
            "code": "CN101080406",
            "name_en": "xinghe"
          },
          {
            "name": "凉城",
            "code": "CN101080407",
            "name_en": "liangcheng"
          },
          {
            "name": "察右前旗",
            "code": "CN101080408",
            "name_en": "chayouqianqi"
          },
          {
            "name": "察右中旗",
            "code": "CN101080409",
            "name_en": "chayouzhongqi"
          },
          {
            "name": "察右后旗",
            "code": "CN101080410",
            "name_en": "chayouhouqi"
          },
          {
            "name": "四子王旗",
            "code": "CN101080411",
            "name_en": "siziwangqi"
          },
          {
            "name": "丰镇",
            "code": "CN101080412",
            "name_en": "fengzhen"
          }
        ]
      },
      {
        "name": "通辽",
        "county": [
          {
            "name": "通辽",
            "code": "CN101080501",
            "name_en": "tongliao"
          },
          {
            "name": "舍伯吐",
            "code": "CN101080502",
            "name_en": "shebotu"
          },
          {
            "name": "科左中旗",
            "code": "CN101080503",
            "name_en": "kezuozhongqi"
          },
          {
            "name": "科左后旗",
            "code": "CN101080504",
            "name_en": "kezuohouqi"
          },
          {
            "name": "青龙山",
            "code": "CN101080505",
            "name_en": "qinglongshan"
          },
          {
            "name": "开鲁",
            "code": "CN101080506",
            "name_en": "kailu"
          },
          {
            "name": "库伦",
            "code": "CN101080507",
            "name_en": "kulun"
          },
          {
            "name": "奈曼",
            "code": "CN101080508",
            "name_en": "naiman"
          },
          {
            "name": "扎鲁特",
            "code": "CN101080509",
            "name_en": "zhalute"
          }
        ]
      },
      {
        "name": "兴安盟",
        "county": [
          {
            "name": "高力板",
            "code": "CN101080510",
            "name_en": "gaoliban"
          }
        ]
      },
      {
        "name": "通辽",
        "county": [
          {
            "name": "巴雅尔吐胡硕",
            "code": "CN101080511",
            "name_en": "bayaertuhushuo"
          }
        ]
      },
      {
        "name": "赤峰",
        "county": [
          {
            "name": "赤峰",
            "code": "CN101080601",
            "name_en": "chifeng"
          },
          {
            "name": "阿鲁旗",
            "code": "CN101080603",
            "name_en": "aluqi"
          },
          {
            "name": "浩尔吐",
            "code": "CN101080604",
            "name_en": "haoertu"
          },
          {
            "name": "巴林左旗",
            "code": "CN101080605",
            "name_en": "balinzuoqi"
          },
          {
            "name": "巴林右旗",
            "code": "CN101080606",
            "name_en": "balinyouqi"
          },
          {
            "name": "林西",
            "code": "CN101080607",
            "name_en": "linxi"
          },
          {
            "name": "克什克腾",
            "code": "CN101080608",
            "name_en": "keshiketeng"
          },
          {
            "name": "翁牛特",
            "code": "CN101080609",
            "name_en": "wengniute"
          },
          {
            "name": "岗子",
            "code": "CN101080610",
            "name_en": "gangzi"
          },
          {
            "name": "喀喇沁",
            "code": "CN101080611",
            "name_en": "kalaqin"
          },
          {
            "name": "八里罕",
            "code": "CN101080612",
            "name_en": "balihan"
          },
          {
            "name": "宁城",
            "code": "CN101080613",
            "name_en": "ningcheng"
          },
          {
            "name": "敖汉",
            "code": "CN101080614",
            "name_en": "aohan"
          },
          {
            "name": "宝国吐",
            "code": "CN101080615",
            "name_en": "baoguotu"
          }
        ]
      },
      {
        "name": "鄂尔多斯",
        "county": [
          {
            "name": "鄂尔多斯",
            "code": "CN101080701",
            "name_en": "eerduosi"
          },
          {
            "name": "达拉特",
            "code": "CN101080703",
            "name_en": "dalate"
          },
          {
            "name": "准格尔",
            "code": "CN101080704",
            "name_en": "zhungeer"
          },
          {
            "name": "鄂前旗",
            "code": "CN101080705",
            "name_en": "eqianqi"
          },
          {
            "name": "河南",
            "code": "CN101080706",
            "name_en": "henan"
          },
          {
            "name": "伊克乌素",
            "code": "CN101080707",
            "name_en": "yikewusu"
          },
          {
            "name": "鄂托克",
            "code": "CN101080708",
            "name_en": "etuoke"
          },
          {
            "name": "杭锦旗",
            "code": "CN101080709",
            "name_en": "hangjinqi"
          },
          {
            "name": "乌审旗",
            "code": "CN101080710",
            "name_en": "wushenqi"
          },
          {
            "name": "伊金霍洛",
            "code": "CN101080711",
            "name_en": "yijinhuoluo"
          },
          {
            "name": "乌审召",
            "code": "CN101080712",
            "name_en": "wushenzhao"
          },
          {
            "name": "东胜",
            "code": "CN101080713",
            "name_en": "dongsheng"
          }
        ]
      },
      {
        "name": "巴彦淖尔",
        "county": [
          {
            "name": "临河",
            "code": "CN101080801",
            "name_en": "linhe"
          },
          {
            "name": "五原",
            "code": "CN101080802",
            "name_en": "wuyuan"
          },
          {
            "name": "磴口",
            "code": "CN101080803",
            "name_en": "dengkou"
          },
          {
            "name": "乌前旗",
            "code": "CN101080804",
            "name_en": "wuqianqi"
          },
          {
            "name": "大佘太",
            "code": "CN101080805",
            "name_en": "dashetai"
          },
          {
            "name": "乌中旗",
            "code": "CN101080806",
            "name_en": "wuzhongqi"
          },
          {
            "name": "乌后旗",
            "code": "CN101080807",
            "name_en": "wuhouqi"
          },
          {
            "name": "海力素",
            "code": "CN101080808",
            "name_en": "hailisu"
          },
          {
            "name": "那仁宝力格",
            "code": "CN101080809",
            "name_en": "narenbaolige"
          },
          {
            "name": "杭锦后旗",
            "code": "CN101080810",
            "name_en": "hangjinhouqi"
          }
        ]
      },
      {
        "name": "锡林郭勒",
        "county": [
          {
            "name": "锡林浩特",
            "code": "CN101080901",
            "name_en": "xilinhaote"
          },
          {
            "name": "二连浩特",
            "code": "CN101080903",
            "name_en": "erlianhaote"
          },
          {
            "name": "阿巴嘎",
            "code": "CN101080904",
            "name_en": "abaga"
          },
          {
            "name": "苏左旗",
            "code": "CN101080906",
            "name_en": "suzuoqi"
          },
          {
            "name": "苏右旗",
            "code": "CN101080907",
            "name_en": "suyouqi"
          },
          {
            "name": "朱日和",
            "code": "CN101080908",
            "name_en": "zhurihe"
          },
          {
            "name": "东乌旗",
            "code": "CN101080909",
            "name_en": "dongwuqi"
          },
          {
            "name": "西乌旗",
            "code": "CN101080910",
            "name_en": "xiwuqi"
          },
          {
            "name": "太仆寺",
            "code": "CN101080911",
            "name_en": "taipusiqi"
          },
          {
            "name": "镶黄旗",
            "code": "CN101080912",
            "name_en": "xianghuang"
          },
          {
            "name": "正镶白旗",
            "code": "CN101080913",
            "name_en": "zhengxiangbaiqi"
          },
          {
            "name": "正蓝旗",
            "code": "CN101080914",
            "name_en": "zhenglanqi"
          },
          {
            "name": "多伦",
            "code": "CN101080915",
            "name_en": "duolun"
          },
          {
            "name": "博克图",
            "code": "CN101080916",
            "name_en": "boketu"
          },
          {
            "name": "乌拉盖",
            "code": "CN101080917",
            "name_en": "wulagai"
          }
        ]
      },
      {
        "name": "呼伦贝尔",
        "county": [
          {
            "name": "海拉尔",
            "code": "CN101081001",
            "name_en": "hailaer"
          },
          {
            "name": "小二沟",
            "code": "CN101081002",
            "name_en": "xiaoergou"
          },
          {
            "name": "阿荣旗",
            "code": "CN101081003",
            "name_en": "arongqi"
          },
          {
            "name": "莫力达瓦",
            "code": "CN101081004",
            "name_en": "molidawa"
          },
          {
            "name": "鄂伦春旗",
            "code": "CN101081005",
            "name_en": "elunchunqi"
          },
          {
            "name": "鄂温克旗",
            "code": "CN101081006",
            "name_en": "ewenkeqi"
          },
          {
            "name": "陈旗",
            "code": "CN101081007",
            "name_en": "chenqi"
          },
          {
            "name": "新左旗",
            "code": "CN101081008",
            "name_en": "xinzuoqi"
          },
          {
            "name": "新右旗",
            "code": "CN101081009",
            "name_en": "xinyouqi"
          },
          {
            "name": "满洲里",
            "code": "CN101081010",
            "name_en": "manzhouli"
          },
          {
            "name": "牙克石",
            "code": "CN101081011",
            "name_en": "yakeshi"
          },
          {
            "name": "扎兰屯",
            "code": "CN101081012",
            "name_en": "zhalantun"
          },
          {
            "name": "额尔古纳",
            "code": "CN101081014",
            "name_en": "eerguna"
          },
          {
            "name": "根河",
            "code": "CN101081015",
            "name_en": "genhe"
          },
          {
            "name": "图里河",
            "code": "CN101081016",
            "name_en": "tulihe"
          }
        ]
      },
      {
        "name": "兴安盟",
        "county": [
          {
            "name": "乌兰浩特",
            "code": "CN101081101",
            "name_en": "wulanhaote"
          },
          {
            "name": "阿尔山",
            "code": "CN101081102",
            "name_en": "aershan"
          },
          {
            "name": "科右中旗",
            "code": "CN101081103",
            "name_en": "keyouzhongqi"
          },
          {
            "name": "胡尔勒",
            "code": "CN101081104",
            "name_en": "huerle"
          },
          {
            "name": "扎赉特",
            "code": "CN101081105",
            "name_en": "zhanlaite"
          },
          {
            "name": "索伦",
            "code": "CN101081106",
            "name_en": "suolun"
          },
          {
            "name": "突泉",
            "code": "CN101081107",
            "name_en": "tuquan"
          }
        ]
      },
      {
        "name": "通辽",
        "county": [
          {
            "name": "霍林郭勒",
            "code": "CN101081108",
            "name_en": "huolinguole"
          }
        ]
      },
      {
        "name": "兴安盟",
        "county": [
          {
            "name": "科右前旗",
            "code": "CN101081109",
            "name_en": "keyouqianqi"
          }
        ]
      },
      {
        "name": "阿拉善盟",
        "county": [
          {
            "name": "阿左旗",
            "code": "CN101081201",
            "name_en": "azuoqi"
          },
          {
            "name": "阿右旗",
            "code": "CN101081202",
            "name_en": "ayouqi"
          },
          {
            "name": "额济纳",
            "code": "CN101081203",
            "name_en": "ejina"
          },
          {
            "name": "拐子湖",
            "code": "CN101081204",
            "name_en": "guanzihu"
          },
          {
            "name": "吉兰太",
            "code": "CN101081205",
            "name_en": "jilantai"
          },
          {
            "name": "锡林高勒",
            "code": "CN101081206",
            "name_en": "xilingaole"
          },
          {
            "name": "头道湖",
            "code": "CN101081207",
            "name_en": "toudaohu"
          },
          {
            "name": "中泉子",
            "code": "CN101081208",
            "name_en": "zhongquanzi"
          },
          {
            "name": "诺尔公",
            "code": "CN101081209",
            "name_en": "nuoergong"
          },
          {
            "name": "雅布赖",
            "code": "CN101081210",
            "name_en": "yabulai"
          },
          {
            "name": "乌斯泰",
            "code": "CN101081211",
            "name_en": "wusitai"
          },
          {
            "name": "孪井滩",
            "code": "CN101081212",
            "name_en": "luanjingtan"
          }
        ]
      }
    ]
  },
  {
    "name": "河北",
    "name_en": "hebei",
    "city": [
      {
        "name": "石家庄",
        "county": [
          {
            "name": "石家庄",
            "code": "CN101090101",
            "name_en": "shijiazhuang"
          },
          {
            "name": "井陉",
            "code": "CN101090102",
            "name_en": "jingxing"
          },
          {
            "name": "正定",
            "code": "CN101090103",
            "name_en": "zhengding"
          },
          {
            "name": "栾城",
            "code": "CN101090104",
            "name_en": "luancheng"
          },
          {
            "name": "行唐",
            "code": "CN101090105",
            "name_en": "xingtang"
          },
          {
            "name": "灵寿",
            "code": "CN101090106",
            "name_en": "lingshou"
          },
          {
            "name": "高邑",
            "code": "CN101090107",
            "name_en": "gaoyi"
          },
          {
            "name": "深泽",
            "code": "CN101090108",
            "name_en": "shenze"
          },
          {
            "name": "赞皇",
            "code": "CN101090109",
            "name_en": "zanhuang"
          },
          {
            "name": "无极",
            "code": "CN101090110",
            "name_en": "wuji"
          },
          {
            "name": "平山",
            "code": "CN101090111",
            "name_en": "pingshan"
          },
          {
            "name": "元氏",
            "code": "CN101090112",
            "name_en": "yuanshi"
          },
          {
            "name": "赵县",
            "code": "CN101090113",
            "name_en": "zhaoxian"
          },
          {
            "name": "辛集",
            "code": "CN101090114",
            "name_en": "xinji"
          },
          {
            "name": "藁城",
            "code": "CN101090115",
            "name_en": "gaocheng"
          },
          {
            "name": "晋州",
            "code": "CN101090116",
            "name_en": "jinzhou"
          },
          {
            "name": "新乐",
            "code": "CN101090117",
            "name_en": "xinle"
          },
          {
            "name": "鹿泉",
            "code": "CN101090118",
            "name_en": "luquan"
          }
        ]
      },
      {
        "name": "保定",
        "county": [
          {
            "name": "保定",
            "code": "CN101090201",
            "name_en": "baoding"
          },
          {
            "name": "满城",
            "code": "CN101090202",
            "name_en": "mancheng"
          },
          {
            "name": "阜平",
            "code": "CN101090203",
            "name_en": "fuping"
          },
          {
            "name": "徐水",
            "code": "CN101090204",
            "name_en": "xushui"
          },
          {
            "name": "唐县",
            "code": "CN101090205",
            "name_en": "tangxian"
          },
          {
            "name": "高阳",
            "code": "CN101090206",
            "name_en": "gaoyang"
          },
          {
            "name": "容城",
            "code": "CN101090207",
            "name_en": "rongcheng"
          },
          {
            "name": "涞源",
            "code": "CN101090209",
            "name_en": "laiyuan"
          },
          {
            "name": "望都",
            "code": "CN101090210",
            "name_en": "wangdu"
          },
          {
            "name": "安新",
            "code": "CN101090211",
            "name_en": "anxin"
          },
          {
            "name": "易县",
            "code": "CN101090212",
            "name_en": "yixian"
          },
          {
            "name": "曲阳",
            "code": "CN101090214",
            "name_en": "quyang"
          },
          {
            "name": "蠡县",
            "code": "CN101090215",
            "name_en": "lixian"
          },
          {
            "name": "顺平",
            "code": "CN101090216",
            "name_en": "shunping"
          },
          {
            "name": "雄县",
            "code": "CN101090217",
            "name_en": "xiongxian"
          },
          {
            "name": "涿州",
            "code": "CN101090218",
            "name_en": "zhuozhou"
          },
          {
            "name": "定州",
            "code": "CN101090219",
            "name_en": "dingzhou"
          },
          {
            "name": "安国",
            "code": "CN101090220",
            "name_en": "anguo"
          },
          {
            "name": "高碑店",
            "code": "CN101090221",
            "name_en": "gaobeidian"
          },
          {
            "name": "涞水",
            "code": "CN101090222",
            "name_en": "laishui"
          },
          {
            "name": "定兴",
            "code": "CN101090223",
            "name_en": "dingxing"
          },
          {
            "name": "清苑",
            "code": "CN101090224",
            "name_en": "qingyuan"
          },
          {
            "name": "博野",
            "code": "CN101090225",
            "name_en": "boye"
          }
        ]
      },
      {
        "name": "张家口",
        "county": [
          {
            "name": "张家口",
            "code": "CN101090301",
            "name_en": "zhangjiakou"
          },
          {
            "name": "宣化",
            "code": "CN101090302",
            "name_en": "xuanhua"
          },
          {
            "name": "张北",
            "code": "CN101090303",
            "name_en": "zhangbei"
          },
          {
            "name": "康保",
            "code": "CN101090304",
            "name_en": "kangbao"
          },
          {
            "name": "沽源",
            "code": "CN101090305",
            "name_en": "guyuan"
          },
          {
            "name": "尚义",
            "code": "CN101090306",
            "name_en": "shangyi"
          },
          {
            "name": "蔚县",
            "code": "CN101090307",
            "name_en": "yuxian"
          },
          {
            "name": "阳原",
            "code": "CN101090308",
            "name_en": "yangyuan"
          },
          {
            "name": "怀安",
            "code": "CN101090309",
            "name_en": "huaian"
          },
          {
            "name": "万全",
            "code": "CN101090310",
            "name_en": "wanquan"
          },
          {
            "name": "怀来",
            "code": "CN101090311",
            "name_en": "huailai"
          },
          {
            "name": "涿鹿",
            "code": "CN101090312",
            "name_en": "zhuolu"
          },
          {
            "name": "赤城",
            "code": "CN101090313",
            "name_en": "chicheng"
          },
          {
            "name": "崇礼",
            "code": "CN101090314",
            "name_en": "chongli"
          }
        ]
      },
      {
        "name": "承德",
        "county": [
          {
            "name": "承德",
            "code": "CN101090402",
            "name_en": "chengde"
          },
          {
            "name": "承德县",
            "code": "CN101090403",
            "name_en": "chengdexian"
          },
          {
            "name": "兴隆",
            "code": "CN101090404",
            "name_en": "xinglong"
          },
          {
            "name": "平泉",
            "code": "CN101090405",
            "name_en": "pingquan"
          },
          {
            "name": "滦平",
            "code": "CN101090406",
            "name_en": "luanping"
          },
          {
            "name": "隆化",
            "code": "CN101090407",
            "name_en": "longhua"
          },
          {
            "name": "丰宁",
            "code": "CN101090408",
            "name_en": "fengning"
          },
          {
            "name": "宽城",
            "code": "CN101090409",
            "name_en": "kuancheng"
          },
          {
            "name": "围场",
            "code": "CN101090410",
            "name_en": "weichang"
          }
        ]
      },
      {
        "name": "唐山",
        "county": [
          {
            "name": "唐山",
            "code": "CN101090501",
            "name_en": "tangshan"
          },
          {
            "name": "丰南",
            "code": "CN101090502",
            "name_en": "fengnan"
          },
          {
            "name": "丰润",
            "code": "CN101090503",
            "name_en": "fengrun"
          },
          {
            "name": "滦县",
            "code": "CN101090504",
            "name_en": "luanxian"
          },
          {
            "name": "滦南",
            "code": "CN101090505",
            "name_en": "luannan"
          },
          {
            "name": "乐亭",
            "code": "CN101090506",
            "name_en": "leting"
          },
          {
            "name": "迁西",
            "code": "CN101090507",
            "name_en": "qianxi"
          },
          {
            "name": "玉田",
            "code": "CN101090508",
            "name_en": "yutian"
          },
          {
            "name": "唐海",
            "code": "CN101090509",
            "name_en": "tanghai"
          },
          {
            "name": "遵化",
            "code": "CN101090510",
            "name_en": "zunhua"
          },
          {
            "name": "迁安",
            "code": "CN101090511",
            "name_en": "qianan"
          },
          {
            "name": "曹妃甸",
            "code": "CN101090512",
            "name_en": "caofeidian"
          }
        ]
      },
      {
        "name": "廊坊",
        "county": [
          {
            "name": "廊坊",
            "code": "CN101090601",
            "name_en": "langfang"
          },
          {
            "name": "固安",
            "code": "CN101090602",
            "name_en": "guan"
          },
          {
            "name": "永清",
            "code": "CN101090603",
            "name_en": "yongqing"
          },
          {
            "name": "香河",
            "code": "CN101090604",
            "name_en": "xianghe"
          },
          {
            "name": "大城",
            "code": "CN101090605",
            "name_en": "dacheng"
          },
          {
            "name": "文安",
            "code": "CN101090606",
            "name_en": "wenan"
          },
          {
            "name": "大厂",
            "code": "CN101090607",
            "name_en": "dachang"
          },
          {
            "name": "霸州",
            "code": "CN101090608",
            "name_en": "bazhou"
          },
          {
            "name": "三河",
            "code": "CN101090609",
            "name_en": "sanhe"
          }
        ]
      },
      {
        "name": "沧州",
        "county": [
          {
            "name": "沧州",
            "code": "CN101090701",
            "name_en": "cangzhou"
          },
          {
            "name": "青县",
            "code": "CN101090702",
            "name_en": "qingxian"
          },
          {
            "name": "东光",
            "code": "CN101090703",
            "name_en": "dongguang"
          },
          {
            "name": "海兴",
            "code": "CN101090704",
            "name_en": "haixing"
          },
          {
            "name": "盐山",
            "code": "CN101090705",
            "name_en": "yanshan"
          },
          {
            "name": "肃宁",
            "code": "CN101090706",
            "name_en": "suning"
          },
          {
            "name": "南皮",
            "code": "CN101090707",
            "name_en": "nanpi"
          },
          {
            "name": "吴桥",
            "code": "CN101090708",
            "name_en": "wuqiao"
          },
          {
            "name": "献县",
            "code": "CN101090709",
            "name_en": "xianxian"
          },
          {
            "name": "孟村",
            "code": "CN101090710",
            "name_en": "mengcun"
          },
          {
            "name": "泊头",
            "code": "CN101090711",
            "name_en": "botou"
          },
          {
            "name": "任丘",
            "code": "CN101090712",
            "name_en": "renqiu"
          },
          {
            "name": "黄骅",
            "code": "CN101090713",
            "name_en": "huanghua"
          },
          {
            "name": "河间",
            "code": "CN101090714",
            "name_en": "hejian"
          },
          {
            "name": "沧县",
            "code": "CN101090716",
            "name_en": "cangxian"
          }
        ]
      },
      {
        "name": "衡水",
        "county": [
          {
            "name": "衡水",
            "code": "CN101090801",
            "name_en": "hengshui"
          },
          {
            "name": "枣强",
            "code": "CN101090802",
            "name_en": "zaoqiang"
          },
          {
            "name": "武邑",
            "code": "CN101090803",
            "name_en": "wuyi"
          },
          {
            "name": "武强",
            "code": "CN101090804",
            "name_en": "wuqiang"
          },
          {
            "name": "饶阳",
            "code": "CN101090805",
            "name_en": "raoyang"
          },
          {
            "name": "安平",
            "code": "CN101090806",
            "name_en": "anping"
          },
          {
            "name": "故城",
            "code": "CN101090807",
            "name_en": "gucheng"
          },
          {
            "name": "景县",
            "code": "CN101090808",
            "name_en": "jingxian"
          },
          {
            "name": "阜城",
            "code": "CN101090809",
            "name_en": "fucheng"
          },
          {
            "name": "冀州",
            "code": "CN101090810",
            "name_en": "jizhou"
          },
          {
            "name": "深州",
            "code": "CN101090811",
            "name_en": "shenzhou"
          }
        ]
      },
      {
        "name": "邢台",
        "county": [
          {
            "name": "邢台",
            "code": "CN101090901",
            "name_en": "xingtai"
          },
          {
            "name": "临城",
            "code": "CN101090902",
            "name_en": "lincheng"
          },
          {
            "name": "内丘",
            "code": "CN101090904",
            "name_en": "neiqiu"
          },
          {
            "name": "柏乡",
            "code": "CN101090905",
            "name_en": "baixiang"
          },
          {
            "name": "隆尧",
            "code": "CN101090906",
            "name_en": "longyao"
          },
          {
            "name": "南和",
            "code": "CN101090907",
            "name_en": "nanhe"
          },
          {
            "name": "宁晋",
            "code": "CN101090908",
            "name_en": "ningjin"
          },
          {
            "name": "巨鹿",
            "code": "CN101090909",
            "name_en": "julu"
          },
          {
            "name": "新河",
            "code": "CN101090910",
            "name_en": "xinhe"
          },
          {
            "name": "广宗",
            "code": "CN101090911",
            "name_en": "guangzong"
          },
          {
            "name": "平乡",
            "code": "CN101090912",
            "name_en": "pingxiang"
          },
          {
            "name": "威县",
            "code": "CN101090913",
            "name_en": "weixian"
          },
          {
            "name": "清河",
            "code": "CN101090914",
            "name_en": "qinghe"
          },
          {
            "name": "临西",
            "code": "CN101090915",
            "name_en": "linxi"
          },
          {
            "name": "南宫",
            "code": "CN101090916",
            "name_en": "nangong"
          },
          {
            "name": "沙河",
            "code": "CN101090917",
            "name_en": "shahe"
          },
          {
            "name": "任县",
            "code": "CN101090918",
            "name_en": "renxian"
          }
        ]
      },
      {
        "name": "邯郸",
        "county": [
          {
            "name": "邯郸",
            "code": "CN101091001",
            "name_en": "handan"
          },
          {
            "name": "峰峰",
            "code": "CN101091002",
            "name_en": "fengfeng"
          },
          {
            "name": "临漳",
            "code": "CN101091003",
            "name_en": "linzhang"
          },
          {
            "name": "成安",
            "code": "CN101091004",
            "name_en": "chengan"
          },
          {
            "name": "大名",
            "code": "CN101091005",
            "name_en": "daming"
          },
          {
            "name": "涉县",
            "code": "CN101091006",
            "name_en": "shexian"
          },
          {
            "name": "磁县",
            "code": "CN101091007",
            "name_en": "cixian"
          },
          {
            "name": "肥乡",
            "code": "CN101091008",
            "name_en": "feixiang"
          },
          {
            "name": "永年",
            "code": "CN101091009",
            "name_en": "yongnian"
          },
          {
            "name": "邱县",
            "code": "CN101091010",
            "name_en": "qiuxian"
          },
          {
            "name": "鸡泽",
            "code": "CN101091011",
            "name_en": "jize"
          },
          {
            "name": "广平",
            "code": "CN101091012",
            "name_en": "guangping"
          },
          {
            "name": "馆陶",
            "code": "CN101091013",
            "name_en": "guantao"
          },
          {
            "name": "魏县",
            "code": "CN101091014",
            "name_en": "weixian"
          },
          {
            "name": "曲周",
            "code": "CN101091015",
            "name_en": "quzhou"
          },
          {
            "name": "武安",
            "code": "CN101091016",
            "name_en": "wuan"
          }
        ]
      },
      {
        "name": "秦皇岛",
        "county": [
          {
            "name": "秦皇岛",
            "code": "CN101091101",
            "name_en": "qinhuangdao"
          },
          {
            "name": "青龙",
            "code": "CN101091102",
            "name_en": "qinglong"
          },
          {
            "name": "昌黎",
            "code": "CN101091103",
            "name_en": "changli"
          },
          {
            "name": "抚宁",
            "code": "CN101091104",
            "name_en": "funing"
          },
          {
            "name": "卢龙",
            "code": "CN101091105",
            "name_en": "lulong"
          },
          {
            "name": "北戴河",
            "code": "CN101091106",
            "name_en": "beidaihe"
          }
        ]
      }
    ]
  },
  {
    "name": "山西",
    "name_en": "shanxi",
    "city": [
      {
        "name": "太原",
        "county": [
          {
            "name": "太原",
            "code": "CN101100101",
            "name_en": "taiyuan"
          },
          {
            "name": "清徐",
            "code": "CN101100102",
            "name_en": "qingxu"
          },
          {
            "name": "阳曲",
            "code": "CN101100103",
            "name_en": "yangqu"
          },
          {
            "name": "娄烦",
            "code": "CN101100104",
            "name_en": "loufan"
          },
          {
            "name": "古交",
            "code": "CN101100105",
            "name_en": "gujiao"
          },
          {
            "name": "尖草坪区",
            "code": "CN101100106",
            "name_en": "jiancaopingqu"
          },
          {
            "name": "小店区",
            "code": "CN101100107",
            "name_en": "xiaodianqu"
          }
        ]
      },
      {
        "name": "大同",
        "county": [
          {
            "name": "大同",
            "code": "CN101100201",
            "name_en": "datong"
          },
          {
            "name": "阳高",
            "code": "CN101100202",
            "name_en": "yanggao"
          },
          {
            "name": "大同县",
            "code": "CN101100203",
            "name_en": "datongxian"
          },
          {
            "name": "天镇",
            "code": "CN101100204",
            "name_en": "tianzhen"
          },
          {
            "name": "广灵",
            "code": "CN101100205",
            "name_en": "guangling"
          },
          {
            "name": "灵丘",
            "code": "CN101100206",
            "name_en": "lingqiu"
          },
          {
            "name": "浑源",
            "code": "CN101100207",
            "name_en": "hunyuan"
          },
          {
            "name": "左云",
            "code": "CN101100208",
            "name_en": "zuoyun"
          }
        ]
      },
      {
        "name": "阳泉",
        "county": [
          {
            "name": "阳泉",
            "code": "CN101100301",
            "name_en": "yangquan"
          },
          {
            "name": "盂县",
            "code": "CN101100302",
            "name_en": "yuxian"
          },
          {
            "name": "平定",
            "code": "CN101100303",
            "name_en": "pingding"
          }
        ]
      },
      {
        "name": "晋中",
        "county": [
          {
            "name": "晋中",
            "code": "CN101100401",
            "name_en": "jinzhong"
          },
          {
            "name": "榆次",
            "code": "CN101100402",
            "name_en": "yuci"
          },
          {
            "name": "榆社",
            "code": "CN101100403",
            "name_en": "yushe"
          },
          {
            "name": "左权",
            "code": "CN101100404",
            "name_en": "zuoquan"
          },
          {
            "name": "和顺",
            "code": "CN101100405",
            "name_en": "heshun"
          },
          {
            "name": "昔阳",
            "code": "CN101100406",
            "name_en": "xiyang"
          },
          {
            "name": "寿阳",
            "code": "CN101100407",
            "name_en": "shouyang"
          },
          {
            "name": "太谷",
            "code": "CN101100408",
            "name_en": "taigu"
          },
          {
            "name": "祁县",
            "code": "CN101100409",
            "name_en": "qixian"
          },
          {
            "name": "平遥",
            "code": "CN101100410",
            "name_en": "pingyao"
          },
          {
            "name": "灵石",
            "code": "CN101100411",
            "name_en": "lingshi"
          },
          {
            "name": "介休",
            "code": "CN101100412",
            "name_en": "jiexiu"
          }
        ]
      },
      {
        "name": "长治",
        "county": [
          {
            "name": "长治",
            "code": "CN101100501",
            "name_en": "changzhi"
          },
          {
            "name": "黎城",
            "code": "CN101100502",
            "name_en": "licheng"
          },
          {
            "name": "屯留",
            "code": "CN101100503",
            "name_en": "tunliu"
          },
          {
            "name": "潞城",
            "code": "CN101100504",
            "name_en": "lucheng"
          },
          {
            "name": "襄垣",
            "code": "CN101100505",
            "name_en": "xiangyuan"
          },
          {
            "name": "平顺",
            "code": "CN101100506",
            "name_en": "pingshun"
          },
          {
            "name": "武乡",
            "code": "CN101100507",
            "name_en": "wuxiang"
          },
          {
            "name": "沁县",
            "code": "CN101100508",
            "name_en": "qinxian"
          },
          {
            "name": "长子",
            "code": "CN101100509",
            "name_en": "zhangzi"
          },
          {
            "name": "沁源",
            "code": "CN101100510",
            "name_en": "qinyuan"
          },
          {
            "name": "壶关",
            "code": "CN101100511",
            "name_en": "huguan"
          }
        ]
      },
      {
        "name": "晋城",
        "county": [
          {
            "name": "晋城",
            "code": "CN101100601",
            "name_en": "jincheng"
          },
          {
            "name": "沁水",
            "code": "CN101100602",
            "name_en": "qinshui"
          },
          {
            "name": "阳城",
            "code": "CN101100603",
            "name_en": "yangcheng"
          },
          {
            "name": "陵川",
            "code": "CN101100604",
            "name_en": "lingchuan"
          },
          {
            "name": "高平",
            "code": "CN101100605",
            "name_en": "gaoping"
          },
          {
            "name": "泽州",
            "code": "CN101100606",
            "name_en": "zezhou"
          }
        ]
      },
      {
        "name": "临汾",
        "county": [
          {
            "name": "临汾",
            "code": "CN101100701",
            "name_en": "linfen"
          },
          {
            "name": "曲沃",
            "code": "CN101100702",
            "name_en": "quwo"
          },
          {
            "name": "永和",
            "code": "CN101100703",
            "name_en": "yonghe"
          },
          {
            "name": "隰县",
            "code": "CN101100704",
            "name_en": "xixian"
          },
          {
            "name": "大宁",
            "code": "CN101100705",
            "name_en": "daning"
          },
          {
            "name": "吉县",
            "code": "CN101100706",
            "name_en": "jixian"
          },
          {
            "name": "襄汾",
            "code": "CN101100707",
            "name_en": "xiangfen"
          },
          {
            "name": "蒲县",
            "code": "CN101100708",
            "name_en": "puxian"
          },
          {
            "name": "汾西",
            "code": "CN101100709",
            "name_en": "fenxi"
          },
          {
            "name": "洪洞",
            "code": "CN101100710",
            "name_en": "hongtong"
          },
          {
            "name": "霍州",
            "code": "CN101100711",
            "name_en": "huozhou"
          },
          {
            "name": "乡宁",
            "code": "CN101100712",
            "name_en": "xiangning"
          },
          {
            "name": "翼城",
            "code": "CN101100713",
            "name_en": "yicheng"
          },
          {
            "name": "侯马",
            "code": "CN101100714",
            "name_en": "houma"
          },
          {
            "name": "浮山",
            "code": "CN101100715",
            "name_en": "fushan"
          },
          {
            "name": "安泽",
            "code": "CN101100716",
            "name_en": "anze"
          },
          {
            "name": "古县",
            "code": "CN101100717",
            "name_en": "guxian"
          }
        ]
      },
      {
        "name": "运城",
        "county": [
          {
            "name": "运城",
            "code": "CN101100801",
            "name_en": "yuncheng"
          },
          {
            "name": "临猗",
            "code": "CN101100802",
            "name_en": "linyi"
          },
          {
            "name": "稷山",
            "code": "CN101100803",
            "name_en": "jishan"
          },
          {
            "name": "万荣",
            "code": "CN101100804",
            "name_en": "wanrong"
          },
          {
            "name": "河津",
            "code": "CN101100805",
            "name_en": "hejin"
          },
          {
            "name": "新绛",
            "code": "CN101100806",
            "name_en": "xinjiang"
          },
          {
            "name": "绛县",
            "code": "CN101100807",
            "name_en": "jiangxian"
          },
          {
            "name": "闻喜",
            "code": "CN101100808",
            "name_en": "wenxi"
          },
          {
            "name": "垣曲",
            "code": "CN101100809",
            "name_en": "yuanqu"
          },
          {
            "name": "永济",
            "code": "CN101100810",
            "name_en": "yongji"
          },
          {
            "name": "芮城",
            "code": "CN101100811",
            "name_en": "ruicheng"
          },
          {
            "name": "夏县",
            "code": "CN101100812",
            "name_en": "xiaxian"
          },
          {
            "name": "平陆",
            "code": "CN101100813",
            "name_en": "pinglu"
          }
        ]
      },
      {
        "name": "朔州",
        "county": [
          {
            "name": "朔州",
            "code": "CN101100901",
            "name_en": "shuozhou"
          },
          {
            "name": "平鲁",
            "code": "CN101100902",
            "name_en": "pinglu"
          },
          {
            "name": "山阴",
            "code": "CN101100903",
            "name_en": "shanyin"
          },
          {
            "name": "右玉",
            "code": "CN101100904",
            "name_en": "youyu"
          },
          {
            "name": "应县",
            "code": "CN101100905",
            "name_en": "yingxian"
          },
          {
            "name": "怀仁",
            "code": "CN101100906",
            "name_en": "huairen"
          }
        ]
      },
      {
        "name": "忻州",
        "county": [
          {
            "name": "忻州",
            "code": "CN101101001",
            "name_en": "xinzhou"
          },
          {
            "name": "定襄",
            "code": "CN101101002",
            "name_en": "dingxiang"
          },
          {
            "name": "五台县",
            "code": "CN101101003",
            "name_en": "wutaixian"
          },
          {
            "name": "河曲",
            "code": "CN101101004",
            "name_en": "hequ"
          },
          {
            "name": "偏关",
            "code": "CN101101005",
            "name_en": "pianguan"
          },
          {
            "name": "神池",
            "code": "CN101101006",
            "name_en": "shenchi"
          },
          {
            "name": "宁武",
            "code": "CN101101007",
            "name_en": "ningwu"
          },
          {
            "name": "代县",
            "code": "CN101101008",
            "name_en": "daixian"
          },
          {
            "name": "繁峙",
            "code": "CN101101009",
            "name_en": "fanshi"
          },
          {
            "name": "五台山",
            "code": "CN101101010",
            "name_en": "wutaishan"
          },
          {
            "name": "保德",
            "code": "CN101101011",
            "name_en": "bode"
          },
          {
            "name": "静乐",
            "code": "CN101101012",
            "name_en": "jingle"
          },
          {
            "name": "岢岚",
            "code": "CN101101013",
            "name_en": "kelan"
          },
          {
            "name": "五寨",
            "code": "CN101101014",
            "name_en": "wuzhai"
          },
          {
            "name": "原平",
            "code": "CN101101015",
            "name_en": "yuanping"
          }
        ]
      },
      {
        "name": "吕梁",
        "county": [
          {
            "name": "吕梁",
            "code": "CN101101100",
            "name_en": "lvliang"
          },
          {
            "name": "离石",
            "code": "CN101101101",
            "name_en": "lishi"
          },
          {
            "name": "临县",
            "code": "CN101101102",
            "name_en": "linxian"
          },
          {
            "name": "兴县",
            "code": "CN101101103",
            "name_en": "xingxian"
          },
          {
            "name": "岚县",
            "code": "CN101101104",
            "name_en": "lanxian"
          },
          {
            "name": "柳林",
            "code": "CN101101105",
            "name_en": "liulin"
          },
          {
            "name": "石楼",
            "code": "CN101101106",
            "name_en": "shilou"
          },
          {
            "name": "方山",
            "code": "CN101101107",
            "name_en": "fangshan"
          },
          {
            "name": "交口",
            "code": "CN101101108",
            "name_en": "jiaokou"
          },
          {
            "name": "中阳",
            "code": "CN101101109",
            "name_en": "zhongyang"
          },
          {
            "name": "孝义",
            "code": "CN101101110",
            "name_en": "xiaoyi"
          },
          {
            "name": "汾阳",
            "code": "CN101101111",
            "name_en": "fenyang"
          },
          {
            "name": "文水",
            "code": "CN101101112",
            "name_en": "wenshui"
          },
          {
            "name": "交城",
            "code": "CN101101113",
            "name_en": "jiaocheng"
          }
        ]
      }
    ]
  },
  {
    "name": "陕西",
    "name_en": "shanxi",
    "city": [
      {
        "name": "西安",
        "county": [
          {
            "name": "西安",
            "code": "CN101110101",
            "name_en": "xian"
          },
          {
            "name": "长安",
            "code": "CN101110102",
            "name_en": "changan"
          },
          {
            "name": "临潼",
            "code": "CN101110103",
            "name_en": "lintong"
          },
          {
            "name": "蓝田",
            "code": "CN101110104",
            "name_en": "lantian"
          },
          {
            "name": "周至",
            "code": "CN101110105",
            "name_en": "zhouzhi"
          },
          {
            "name": "户县",
            "code": "CN101110106",
            "name_en": "huxian"
          },
          {
            "name": "高陵",
            "code": "CN101110107",
            "name_en": "gaoling"
          }
        ]
      },
      {
        "name": "咸阳",
        "county": [
          {
            "name": "咸阳",
            "code": "CN101110200",
            "name_en": "xianyang"
          },
          {
            "name": "三原",
            "code": "CN101110201",
            "name_en": "sanyuan"
          },
          {
            "name": "礼泉",
            "code": "CN101110202",
            "name_en": "liquan"
          },
          {
            "name": "永寿",
            "code": "CN101110203",
            "name_en": "yongshou"
          },
          {
            "name": "淳化",
            "code": "CN101110204",
            "name_en": "chunhua"
          },
          {
            "name": "泾阳",
            "code": "CN101110205",
            "name_en": "jingyang"
          },
          {
            "name": "武功",
            "code": "CN101110206",
            "name_en": "wugong"
          },
          {
            "name": "乾县",
            "code": "CN101110207",
            "name_en": "qianxian"
          },
          {
            "name": "彬县",
            "code": "CN101110208",
            "name_en": "binxian"
          },
          {
            "name": "长武",
            "code": "CN101110209",
            "name_en": "changwu"
          },
          {
            "name": "旬邑",
            "code": "CN101110210",
            "name_en": "xunyi"
          },
          {
            "name": "兴平",
            "code": "CN101110211",
            "name_en": "xingping"
          }
        ]
      },
      {
        "name": "延安",
        "county": [
          {
            "name": "延安",
            "code": "CN101110300",
            "name_en": "yanan"
          },
          {
            "name": "延长",
            "code": "CN101110301",
            "name_en": "yanchang"
          },
          {
            "name": "延川",
            "code": "CN101110302",
            "name_en": "yanchuan"
          },
          {
            "name": "子长",
            "code": "CN101110303",
            "name_en": "zichang"
          },
          {
            "name": "宜川",
            "code": "CN101110304",
            "name_en": "yichuan"
          },
          {
            "name": "富县",
            "code": "CN101110305",
            "name_en": "fuxian"
          },
          {
            "name": "志丹",
            "code": "CN101110306",
            "name_en": "zhidan"
          },
          {
            "name": "安塞",
            "code": "CN101110307",
            "name_en": "ansai"
          },
          {
            "name": "甘泉",
            "code": "CN101110308",
            "name_en": "ganquan"
          },
          {
            "name": "洛川",
            "code": "CN101110309",
            "name_en": "luochuan"
          },
          {
            "name": "黄陵",
            "code": "CN101110310",
            "name_en": "huangling"
          },
          {
            "name": "黄龙",
            "code": "CN101110311",
            "name_en": "huanglong"
          },
          {
            "name": "吴起",
            "code": "CN101110312",
            "name_en": "wuqi"
          }
        ]
      },
      {
        "name": "榆林",
        "county": [
          {
            "name": "榆林",
            "code": "CN101110401",
            "name_en": "yulin"
          },
          {
            "name": "府谷",
            "code": "CN101110402",
            "name_en": "fugu"
          },
          {
            "name": "神木",
            "code": "CN101110403",
            "name_en": "shenmu"
          },
          {
            "name": "佳县",
            "code": "CN101110404",
            "name_en": "jiaxian"
          },
          {
            "name": "定边",
            "code": "CN101110405",
            "name_en": "dingbian"
          },
          {
            "name": "靖边",
            "code": "CN101110406",
            "name_en": "jingbian"
          },
          {
            "name": "横山",
            "code": "CN101110407",
            "name_en": "hengshan"
          },
          {
            "name": "米脂",
            "code": "CN101110408",
            "name_en": "mizhi"
          },
          {
            "name": "子洲",
            "code": "CN101110409",
            "name_en": "zizhou"
          },
          {
            "name": "绥德",
            "code": "CN101110410",
            "name_en": "suide"
          },
          {
            "name": "吴堡",
            "code": "CN101110411",
            "name_en": "wubu"
          },
          {
            "name": "清涧",
            "code": "CN101110412",
            "name_en": "qingjian"
          },
          {
            "name": "榆阳",
            "code": "CN101110413",
            "name_en": "yuyang"
          }
        ]
      },
      {
        "name": "渭南",
        "county": [
          {
            "name": "渭南",
            "code": "CN101110501",
            "name_en": "weinan"
          },
          {
            "name": "华县",
            "code": "CN101110502",
            "name_en": "huaxian"
          },
          {
            "name": "潼关",
            "code": "CN101110503",
            "name_en": "tongguan"
          },
          {
            "name": "大荔",
            "code": "CN101110504",
            "name_en": "dali"
          },
          {
            "name": "白水",
            "code": "CN101110505",
            "name_en": "baishui"
          },
          {
            "name": "富平",
            "code": "CN101110506",
            "name_en": "fuping"
          },
          {
            "name": "蒲城",
            "code": "CN101110507",
            "name_en": "pucheng"
          },
          {
            "name": "澄城",
            "code": "CN101110508",
            "name_en": "chengcheng"
          },
          {
            "name": "合阳",
            "code": "CN101110509",
            "name_en": "heyang"
          },
          {
            "name": "韩城",
            "code": "CN101110510",
            "name_en": "hancheng"
          },
          {
            "name": "华阴",
            "code": "CN101110511",
            "name_en": "huayin"
          }
        ]
      },
      {
        "name": "商洛",
        "county": [
          {
            "name": "商洛",
            "code": "CN101110601",
            "name_en": "shangluo"
          },
          {
            "name": "洛南",
            "code": "CN101110602",
            "name_en": "luonan"
          },
          {
            "name": "柞水",
            "code": "CN101110603",
            "name_en": "zhashui"
          },
          {
            "name": "商州",
            "code": "CN101110604",
            "name_en": "shangzhou"
          },
          {
            "name": "镇安",
            "code": "CN101110605",
            "name_en": "zhenan"
          },
          {
            "name": "丹凤",
            "code": "CN101110606",
            "name_en": "danfeng"
          },
          {
            "name": "商南",
            "code": "CN101110607",
            "name_en": "shangnan"
          },
          {
            "name": "山阳",
            "code": "CN101110608",
            "name_en": "shanyang"
          }
        ]
      },
      {
        "name": "安康",
        "county": [
          {
            "name": "安康",
            "code": "CN101110701",
            "name_en": "ankang"
          },
          {
            "name": "紫阳",
            "code": "CN101110702",
            "name_en": "ziyang"
          },
          {
            "name": "石泉",
            "code": "CN101110703",
            "name_en": "shiquan"
          },
          {
            "name": "汉阴",
            "code": "CN101110704",
            "name_en": "hanyin"
          },
          {
            "name": "旬阳",
            "code": "CN101110705",
            "name_en": "xunyang"
          },
          {
            "name": "岚皋",
            "code": "CN101110706",
            "name_en": "langao"
          },
          {
            "name": "平利",
            "code": "CN101110707",
            "name_en": "pingli"
          },
          {
            "name": "白河",
            "code": "CN101110708",
            "name_en": "baihe"
          },
          {
            "name": "镇坪",
            "code": "CN101110709",
            "name_en": "zhenping"
          },
          {
            "name": "宁陕",
            "code": "CN101110710",
            "name_en": "ningshan"
          }
        ]
      },
      {
        "name": "汉中",
        "county": [
          {
            "name": "汉中",
            "code": "CN101110801",
            "name_en": "hanzhong"
          },
          {
            "name": "略阳",
            "code": "CN101110802",
            "name_en": "lueyang"
          },
          {
            "name": "勉县",
            "code": "CN101110803",
            "name_en": "mianxian"
          },
          {
            "name": "留坝",
            "code": "CN101110804",
            "name_en": "liuba"
          },
          {
            "name": "洋县",
            "code": "CN101110805",
            "name_en": "yangxian"
          },
          {
            "name": "城固",
            "code": "CN101110806",
            "name_en": "chenggu"
          },
          {
            "name": "西乡",
            "code": "CN101110807",
            "name_en": "xixiang"
          },
          {
            "name": "佛坪",
            "code": "CN101110808",
            "name_en": "fuoping"
          },
          {
            "name": "宁强",
            "code": "CN101110809",
            "name_en": "ningqiang"
          },
          {
            "name": "南郑",
            "code": "CN101110810",
            "name_en": "nanzheng"
          },
          {
            "name": "镇巴",
            "code": "CN101110811",
            "name_en": "zhenba"
          }
        ]
      },
      {
        "name": "宝鸡",
        "county": [
          {
            "name": "宝鸡",
            "code": "CN101110901",
            "name_en": "baoji"
          },
          {
            "name": "千阳",
            "code": "CN101110903",
            "name_en": "qianyang"
          },
          {
            "name": "麟游",
            "code": "CN101110904",
            "name_en": "linyou"
          },
          {
            "name": "岐山",
            "code": "CN101110905",
            "name_en": "qishan"
          },
          {
            "name": "凤翔",
            "code": "CN101110906",
            "name_en": "fengxiang"
          },
          {
            "name": "扶风",
            "code": "CN101110907",
            "name_en": "fufeng"
          },
          {
            "name": "眉县",
            "code": "CN101110908",
            "name_en": "meixian"
          },
          {
            "name": "太白",
            "code": "CN101110909",
            "name_en": "taibai"
          },
          {
            "name": "凤县",
            "code": "CN101110910",
            "name_en": "fengxian"
          },
          {
            "name": "陇县",
            "code": "CN101110911",
            "name_en": "longxian"
          },
          {
            "name": "陈仓",
            "code": "CN101110912",
            "name_en": "chencang"
          }
        ]
      },
      {
        "name": "铜川",
        "county": [
          {
            "name": "铜川",
            "code": "CN101111001",
            "name_en": "tongchuan"
          },
          {
            "name": "耀县",
            "code": "CN101111002",
            "name_en": "yaoxian"
          },
          {
            "name": "宜君",
            "code": "CN101111003",
            "name_en": "yijun"
          },
          {
            "name": "耀州",
            "code": "CN101111004",
            "name_en": "yaozhou"
          }
        ]
      },
      {
        "name": "杨凌",
        "county": [
          {
            "name": "杨凌",
            "code": "CN101111101",
            "name_en": "yangling"
          }
        ]
      }
    ]
  },
  {
    "name": "山东",
    "name_en": "shandong",
    "city": [
      {
        "name": "济南",
        "county": [
          {
            "name": "济南",
            "code": "CN101120101",
            "name_en": "jinan"
          },
          {
            "name": "长清",
            "code": "CN101120102",
            "name_en": "changqing"
          },
          {
            "name": "商河",
            "code": "CN101120103",
            "name_en": "shanghe"
          },
          {
            "name": "章丘",
            "code": "CN101120104",
            "name_en": "zhangqiu"
          },
          {
            "name": "平阴",
            "code": "CN101120105",
            "name_en": "pingyin"
          },
          {
            "name": "济阳",
            "code": "CN101120106",
            "name_en": "jiyang"
          }
        ]
      },
      {
        "name": "青岛",
        "county": [
          {
            "name": "青岛",
            "code": "CN101120201",
            "name_en": "qingdao"
          },
          {
            "name": "崂山",
            "code": "CN101120202",
            "name_en": "laoshan"
          },
          {
            "name": "即墨",
            "code": "CN101120204",
            "name_en": "jimo"
          },
          {
            "name": "胶州",
            "code": "CN101120205",
            "name_en": "jiaozhou"
          },
          {
            "name": "黄岛",
            "code": "CN101120206",
            "name_en": "huangdao"
          },
          {
            "name": "莱西",
            "code": "CN101120207",
            "name_en": "laixi"
          },
          {
            "name": "平度",
            "code": "CN101120208",
            "name_en": "pingdu"
          }
        ]
      },
      {
        "name": "淄博",
        "county": [
          {
            "name": "淄博",
            "code": "CN101120301",
            "name_en": "zibo"
          },
          {
            "name": "淄川",
            "code": "CN101120302",
            "name_en": "zichuan"
          },
          {
            "name": "博山",
            "code": "CN101120303",
            "name_en": "boshan"
          },
          {
            "name": "高青",
            "code": "CN101120304",
            "name_en": "gaoqing"
          },
          {
            "name": "周村",
            "code": "CN101120305",
            "name_en": "zhoucun"
          },
          {
            "name": "沂源",
            "code": "CN101120306",
            "name_en": "yiyuan"
          },
          {
            "name": "桓台",
            "code": "CN101120307",
            "name_en": "huantai"
          },
          {
            "name": "临淄",
            "code": "CN101120308",
            "name_en": "linzi"
          }
        ]
      },
      {
        "name": "德州",
        "county": [
          {
            "name": "德州",
            "code": "CN101120401",
            "name_en": "dezhou"
          },
          {
            "name": "武城",
            "code": "CN101120402",
            "name_en": "wucheng"
          },
          {
            "name": "临邑",
            "code": "CN101120403",
            "name_en": "linyi"
          },
          {
            "name": "陵县",
            "code": "CN101120404",
            "name_en": "lingxian"
          },
          {
            "name": "齐河",
            "code": "CN101120405",
            "name_en": "qihe"
          },
          {
            "name": "乐陵",
            "code": "CN101120406",
            "name_en": "leling"
          },
          {
            "name": "庆云",
            "code": "CN101120407",
            "name_en": "qingyun"
          },
          {
            "name": "平原",
            "code": "CN101120408",
            "name_en": "pingyuan"
          },
          {
            "name": "宁津",
            "code": "CN101120409",
            "name_en": "ningjin"
          },
          {
            "name": "夏津",
            "code": "CN101120410",
            "name_en": "xiajin"
          },
          {
            "name": "禹城",
            "code": "CN101120411",
            "name_en": "yucheng"
          }
        ]
      },
      {
        "name": "烟台",
        "county": [
          {
            "name": "烟台",
            "code": "CN101120501",
            "name_en": "yantai"
          },
          {
            "name": "莱州",
            "code": "CN101120502",
            "name_en": "laizhou"
          },
          {
            "name": "长岛",
            "code": "CN101120503",
            "name_en": "changdao"
          },
          {
            "name": "蓬莱",
            "code": "CN101120504",
            "name_en": "penglai"
          },
          {
            "name": "龙口",
            "code": "CN101120505",
            "name_en": "longkou"
          },
          {
            "name": "招远",
            "code": "CN101120506",
            "name_en": "zhaoyuan"
          },
          {
            "name": "栖霞",
            "code": "CN101120507",
            "name_en": "qixia"
          },
          {
            "name": "福山",
            "code": "CN101120508",
            "name_en": "fushan"
          },
          {
            "name": "牟平",
            "code": "CN101120509",
            "name_en": "moup"
          },
          {
            "name": "莱阳",
            "code": "CN101120510",
            "name_en": "laiyang"
          },
          {
            "name": "海阳",
            "code": "CN101120511",
            "name_en": "haiyang"
          }
        ]
      },
      {
        "name": "潍坊",
        "county": [
          {
            "name": "潍坊",
            "code": "CN101120601",
            "name_en": "weifang"
          },
          {
            "name": "青州",
            "code": "CN101120602",
            "name_en": "qingzhou"
          },
          {
            "name": "寿光",
            "code": "CN101120603",
            "name_en": "shouguang"
          },
          {
            "name": "临朐",
            "code": "CN101120604",
            "name_en": "linqu"
          },
          {
            "name": "昌乐",
            "code": "CN101120605",
            "name_en": "changle"
          },
          {
            "name": "昌邑",
            "code": "CN101120606",
            "name_en": "changyi"
          },
          {
            "name": "安丘",
            "code": "CN101120607",
            "name_en": "anqiu"
          },
          {
            "name": "高密",
            "code": "CN101120608",
            "name_en": "gaomi"
          },
          {
            "name": "诸城",
            "code": "CN101120609",
            "name_en": "zhucheng"
          }
        ]
      },
      {
        "name": "济宁",
        "county": [
          {
            "name": "济宁",
            "code": "CN101120701",
            "name_en": "jining"
          },
          {
            "name": "嘉祥",
            "code": "CN101120702",
            "name_en": "jiaxiang"
          },
          {
            "name": "微山",
            "code": "CN101120703",
            "name_en": "weishan"
          },
          {
            "name": "鱼台",
            "code": "CN101120704",
            "name_en": "yutai"
          },
          {
            "name": "兖州",
            "code": "CN101120705",
            "name_en": "yanzhou"
          },
          {
            "name": "金乡",
            "code": "CN101120706",
            "name_en": "jinxiang"
          },
          {
            "name": "汶上",
            "code": "CN101120707",
            "name_en": "wenshang"
          },
          {
            "name": "泗水",
            "code": "CN101120708",
            "name_en": "sishui"
          },
          {
            "name": "梁山",
            "code": "CN101120709",
            "name_en": "liangshan"
          },
          {
            "name": "曲阜",
            "code": "CN101120710",
            "name_en": "qufu"
          },
          {
            "name": "邹城",
            "code": "CN101120711",
            "name_en": "zoucheng"
          }
        ]
      },
      {
        "name": "泰安",
        "county": [
          {
            "name": "泰安",
            "code": "CN101120801",
            "name_en": "taian"
          },
          {
            "name": "新泰",
            "code": "CN101120802",
            "name_en": "xintai"
          },
          {
            "name": "肥城",
            "code": "CN101120804",
            "name_en": "feicheng"
          },
          {
            "name": "东平",
            "code": "CN101120805",
            "name_en": "dongping"
          },
          {
            "name": "宁阳",
            "code": "CN101120806",
            "name_en": "ningyang"
          }
        ]
      },
      {
        "name": "临沂",
        "county": [
          {
            "name": "临沂",
            "code": "CN101120901",
            "name_en": "linyi"
          },
          {
            "name": "莒南",
            "code": "CN101120902",
            "name_en": "junan"
          },
          {
            "name": "沂南",
            "code": "CN101120903",
            "name_en": "yinan"
          },
          {
            "name": "兰陵",
            "code": "CN101120904",
            "name_en": "lanling"
          },
          {
            "name": "临沭",
            "code": "CN101120905",
            "name_en": "linshu"
          },
          {
            "name": "郯城",
            "code": "CN101120906",
            "name_en": "tancheng"
          },
          {
            "name": "蒙阴",
            "code": "CN101120907",
            "name_en": "mengyin"
          },
          {
            "name": "平邑",
            "code": "CN101120908",
            "name_en": "pingyi"
          },
          {
            "name": "费县",
            "code": "CN101120909",
            "name_en": "feixian"
          },
          {
            "name": "沂水",
            "code": "CN101120910",
            "name_en": "yishui"
          }
        ]
      },
      {
        "name": "菏泽",
        "county": [
          {
            "name": "菏泽",
            "code": "CN101121001",
            "name_en": "heze"
          },
          {
            "name": "鄄城",
            "code": "CN101121002",
            "name_en": "juancheng"
          },
          {
            "name": "郓城",
            "code": "CN101121003",
            "name_en": "yuncheng"
          },
          {
            "name": "东明",
            "code": "CN101121004",
            "name_en": "dongming"
          },
          {
            "name": "定陶",
            "code": "CN101121005",
            "name_en": "dingtao"
          },
          {
            "name": "巨野",
            "code": "CN101121006",
            "name_en": "juye"
          },
          {
            "name": "曹县",
            "code": "CN101121007",
            "name_en": "caoxian"
          },
          {
            "name": "成武",
            "code": "CN101121008",
            "name_en": "chengwu"
          },
          {
            "name": "单县",
            "code": "CN101121009",
            "name_en": "shanxian"
          }
        ]
      },
      {
        "name": "滨州",
        "county": [
          {
            "name": "滨州",
            "code": "CN101121101",
            "name_en": "binzhou"
          },
          {
            "name": "博兴",
            "code": "CN101121102",
            "name_en": "boxing"
          },
          {
            "name": "无棣",
            "code": "CN101121103",
            "name_en": "wudi"
          },
          {
            "name": "阳信",
            "code": "CN101121104",
            "name_en": "yangxin"
          },
          {
            "name": "惠民",
            "code": "CN101121105",
            "name_en": "huimin"
          },
          {
            "name": "沾化",
            "code": "CN101121106",
            "name_en": "zhanhua"
          },
          {
            "name": "邹平",
            "code": "CN101121107",
            "name_en": "zouping"
          }
        ]
      },
      {
        "name": "东营",
        "county": [
          {
            "name": "东营",
            "code": "CN101121201",
            "name_en": "dongying"
          },
          {
            "name": "河口",
            "code": "CN101121202",
            "name_en": "hekou"
          },
          {
            "name": "垦利",
            "code": "CN101121203",
            "name_en": "kenli"
          },
          {
            "name": "利津",
            "code": "CN101121204",
            "name_en": "lijin"
          },
          {
            "name": "广饶",
            "code": "CN101121205",
            "name_en": "guangrao"
          }
        ]
      },
      {
        "name": "威海",
        "county": [
          {
            "name": "威海",
            "code": "CN101121301",
            "name_en": "weihai"
          },
          {
            "name": "文登",
            "code": "CN101121302",
            "name_en": "wendeng"
          },
          {
            "name": "荣成",
            "code": "CN101121303",
            "name_en": "rongcheng"
          },
          {
            "name": "乳山",
            "code": "CN101121304",
            "name_en": "rushan"
          },
          {
            "name": "成山头",
            "code": "CN101121305",
            "name_en": "chengshantou"
          },
          {
            "name": "石岛",
            "code": "CN101121306",
            "name_en": "shidao"
          }
        ]
      },
      {
        "name": "枣庄",
        "county": [
          {
            "name": "枣庄",
            "code": "CN101121401",
            "name_en": "zaozhuang"
          },
          {
            "name": "薛城",
            "code": "CN101121402",
            "name_en": "xuecheng"
          },
          {
            "name": "峄城",
            "code": "CN101121403",
            "name_en": "yicheng"
          },
          {
            "name": "台儿庄",
            "code": "CN101121404",
            "name_en": "taierzhuang"
          },
          {
            "name": "滕州",
            "code": "CN101121405",
            "name_en": "tengzhou"
          }
        ]
      },
      {
        "name": "日照",
        "county": [
          {
            "name": "日照",
            "code": "CN101121501",
            "name_en": "rizhao"
          },
          {
            "name": "五莲",
            "code": "CN101121502",
            "name_en": "wulian"
          },
          {
            "name": "莒县",
            "code": "CN101121503",
            "name_en": "juxian"
          }
        ]
      },
      {
        "name": "莱芜",
        "county": [
          {
            "name": "莱芜",
            "code": "CN101121601",
            "name_en": "laiwu"
          }
        ]
      },
      {
        "name": "聊城",
        "county": [
          {
            "name": "聊城",
            "code": "CN101121701",
            "name_en": "liaocheng"
          },
          {
            "name": "冠县",
            "code": "CN101121702",
            "name_en": "guanxian"
          },
          {
            "name": "阳谷",
            "code": "CN101121703",
            "name_en": "yanggu"
          },
          {
            "name": "高唐",
            "code": "CN101121704",
            "name_en": "gaotang"
          },
          {
            "name": "茌平",
            "code": "CN101121705",
            "name_en": "chiping"
          },
          {
            "name": "东阿",
            "code": "CN101121706",
            "name_en": "donge"
          },
          {
            "name": "临清",
            "code": "CN101121707",
            "name_en": "linqing"
          },
          {
            "name": "莘县",
            "code": "CN101121709",
            "name_en": "shenxian"
          }
        ]
      }
    ]
  },
  {
    "name": "新疆",
    "name_en": "xinjiang",
    "city": [
      {
        "name": "乌鲁木齐",
        "county": [
          {
            "name": "乌鲁木齐",
            "code": "CN101130101",
            "name_en": "wulumuqi"
          },
          {
            "name": "小渠子",
            "code": "CN101130103",
            "name_en": "xiaoquzi"
          },
          {
            "name": "达坂城",
            "code": "CN101130105",
            "name_en": "dabancheng"
          },
          {
            "name": "乌鲁木齐牧试站",
            "code": "CN101130108",
            "name_en": "wulumuqimushizhan"
          },
          {
            "name": "天池",
            "code": "CN101130109",
            "name_en": "tianchi"
          },
          {
            "name": "白杨沟",
            "code": "CN101130110",
            "name_en": "baiyanggou"
          }
        ]
      },
      {
        "name": "克拉玛依",
        "county": [
          {
            "name": "克拉玛依",
            "code": "CN101130201",
            "name_en": "kelamayi"
          },
          {
            "name": "乌尔禾",
            "code": "CN101130202",
            "name_en": "wuerhe"
          },
          {
            "name": "白碱滩",
            "code": "CN101130203",
            "name_en": "baijiantan"
          }
        ]
      },
      {
        "name": "石河子",
        "county": [
          {
            "name": "石河子",
            "code": "CN101130301",
            "name_en": "shihezi"
          },
          {
            "name": "炮台",
            "code": "CN101130302",
            "name_en": "paotai"
          },
          {
            "name": "莫索湾",
            "code": "CN101130303",
            "name_en": "mosuowan"
          }
        ]
      },
      {
        "name": "昌吉",
        "county": [
          {
            "name": "昌吉",
            "code": "CN101130401",
            "name_en": "changji"
          },
          {
            "name": "呼图壁",
            "code": "CN101130402",
            "name_en": "hutubi"
          },
          {
            "name": "米泉",
            "code": "CN101130403",
            "name_en": "miquan"
          },
          {
            "name": "阜康",
            "code": "CN101130404",
            "name_en": "fukang"
          },
          {
            "name": "吉木萨尔",
            "code": "CN101130405",
            "name_en": "jimusaer"
          },
          {
            "name": "奇台",
            "code": "CN101130406",
            "name_en": "qitai"
          },
          {
            "name": "玛纳斯",
            "code": "CN101130407",
            "name_en": "manasi"
          },
          {
            "name": "木垒",
            "code": "CN101130408",
            "name_en": "mulei"
          },
          {
            "name": "蔡家湖",
            "code": "CN101130409",
            "name_en": "caijiahu"
          }
        ]
      },
      {
        "name": "吐鲁番",
        "county": [
          {
            "name": "吐鲁番",
            "code": "CN101130501",
            "name_en": "tulufan"
          },
          {
            "name": "托克逊",
            "code": "CN101130502",
            "name_en": "tuokexun"
          },
          {
            "name": "鄯善",
            "code": "CN101130504",
            "name_en": "shanshan"
          }
        ]
      },
      {
        "name": "巴音郭楞",
        "county": [
          {
            "name": "库尔勒",
            "code": "CN101130601",
            "name_en": "kuerle"
          },
          {
            "name": "轮台",
            "code": "CN101130602",
            "name_en": "luntai"
          },
          {
            "name": "尉犁",
            "code": "CN101130603",
            "name_en": "yuli"
          },
          {
            "name": "若羌",
            "code": "CN101130604",
            "name_en": "ruoqiang"
          },
          {
            "name": "且末",
            "code": "CN101130605",
            "name_en": "qiemo"
          },
          {
            "name": "和静",
            "code": "CN101130606",
            "name_en": "hejing"
          },
          {
            "name": "焉耆",
            "code": "CN101130607",
            "name_en": "yanqi"
          },
          {
            "name": "和硕",
            "code": "CN101130608",
            "name_en": "shuo"
          },
          {
            "name": "巴音布鲁克",
            "code": "CN101130610",
            "name_en": "bayinbuluke"
          },
          {
            "name": "铁干里克",
            "code": "CN101130611",
            "name_en": "tieganlike"
          },
          {
            "name": "博湖",
            "code": "CN101130612",
            "name_en": "bohu"
          },
          {
            "name": "塔中",
            "code": "CN101130613",
            "name_en": "tazhong"
          },
          {
            "name": "巴仑台",
            "code": "CN101130614",
            "name_en": "baluntai"
          }
        ]
      },
      {
        "name": "阿拉尔",
        "county": [
          {
            "name": "阿拉尔",
            "code": "CN101130701",
            "name_en": "alaer"
          }
        ]
      },
      {
        "name": "阿克苏",
        "county": [
          {
            "name": "阿克苏",
            "code": "CN101130801",
            "name_en": "akesu"
          },
          {
            "name": "乌什",
            "code": "CN101130802",
            "name_en": "wushi"
          },
          {
            "name": "温宿",
            "code": "CN101130803",
            "name_en": "wensu"
          },
          {
            "name": "拜城",
            "code": "CN101130804",
            "name_en": "baicheng"
          },
          {
            "name": "新和",
            "code": "CN101130805",
            "name_en": "xinhe"
          },
          {
            "name": "沙雅",
            "code": "CN101130806",
            "name_en": "shaya"
          },
          {
            "name": "库车",
            "code": "CN101130807",
            "name_en": "kuche"
          },
          {
            "name": "柯坪",
            "code": "CN101130808",
            "name_en": "keping"
          },
          {
            "name": "阿瓦提",
            "code": "CN101130809",
            "name_en": "awati"
          }
        ]
      },
      {
        "name": "喀什",
        "county": [
          {
            "name": "喀什",
            "code": "CN101130901",
            "name_en": "kashi"
          },
          {
            "name": "英吉沙",
            "code": "CN101130902",
            "name_en": "yingjisha"
          },
          {
            "name": "塔什库尔干",
            "code": "CN101130903",
            "name_en": "tashikuergan"
          },
          {
            "name": "麦盖提",
            "code": "CN101130904",
            "name_en": "maigaiti"
          },
          {
            "name": "莎车",
            "code": "CN101130905",
            "name_en": "shache"
          },
          {
            "name": "叶城",
            "code": "CN101130906",
            "name_en": "yecheng"
          },
          {
            "name": "泽普",
            "code": "CN101130907",
            "name_en": "zepu"
          },
          {
            "name": "巴楚",
            "code": "CN101130908",
            "name_en": "bachu"
          },
          {
            "name": "岳普湖",
            "code": "CN101130909",
            "name_en": "yuepuhu"
          },
          {
            "name": "伽师",
            "code": "CN101130910",
            "name_en": "jiashi"
          },
          {
            "name": "疏附",
            "code": "CN101130911",
            "name_en": "shufu"
          },
          {
            "name": "疏勒",
            "code": "CN101130912",
            "name_en": "shule"
          }
        ]
      },
      {
        "name": "伊犁",
        "county": [
          {
            "name": "伊宁",
            "code": "CN101131001",
            "name_en": "yining"
          },
          {
            "name": "察布查尔",
            "code": "CN101131002",
            "name_en": "chabuchaer"
          },
          {
            "name": "尼勒克",
            "code": "CN101131003",
            "name_en": "nileke"
          },
          {
            "name": "伊宁县",
            "code": "CN101131004",
            "name_en": "yiningxian"
          },
          {
            "name": "巩留",
            "code": "CN101131005",
            "name_en": "gongliu"
          },
          {
            "name": "新源",
            "code": "CN101131006",
            "name_en": "xinyuan"
          },
          {
            "name": "昭苏",
            "code": "CN101131007",
            "name_en": "zhaosu"
          },
          {
            "name": "特克斯",
            "code": "CN101131008",
            "name_en": "tekesi"
          },
          {
            "name": "霍城",
            "code": "CN101131009",
            "name_en": "huocheng"
          },
          {
            "name": "霍尔果斯",
            "code": "CN101131010",
            "name_en": "huoerguosi"
          },
          {
            "name": "奎屯",
            "code": "CN101131011",
            "name_en": "kuitunshi"
          }
        ]
      },
      {
        "name": "塔城",
        "county": [
          {
            "name": "塔城",
            "code": "CN101131101",
            "name_en": "tacheng"
          },
          {
            "name": "裕民",
            "code": "CN101131102",
            "name_en": "yumin"
          },
          {
            "name": "额敏",
            "code": "CN101131103",
            "name_en": "emin"
          },
          {
            "name": "和布克赛尔",
            "code": "CN101131104",
            "name_en": "hebukesaier"
          },
          {
            "name": "托里",
            "code": "CN101131105",
            "name_en": "tuoli"
          },
          {
            "name": "乌苏",
            "code": "CN101131106",
            "name_en": "wusu"
          },
          {
            "name": "沙湾",
            "code": "CN101131107",
            "name_en": "shawan"
          }
        ]
      },
      {
        "name": "哈密",
        "county": [
          {
            "name": "哈密",
            "code": "CN101131201",
            "name_en": "hami"
          },
          {
            "name": "巴里坤",
            "code": "CN101131203",
            "name_en": "balikun"
          },
          {
            "name": "伊吾",
            "code": "CN101131204",
            "name_en": "yiwu"
          }
        ]
      },
      {
        "name": "和田",
        "county": [
          {
            "name": "和田",
            "code": "CN101131301",
            "name_en": "hetian"
          },
          {
            "name": "皮山",
            "code": "CN101131302",
            "name_en": "pishan"
          },
          {
            "name": "策勒",
            "code": "CN101131303",
            "name_en": "cele"
          },
          {
            "name": "墨玉",
            "code": "CN101131304",
            "name_en": "moyu"
          },
          {
            "name": "洛浦",
            "code": "CN101131305",
            "name_en": "luopu"
          },
          {
            "name": "民丰",
            "code": "CN101131306",
            "name_en": "minfeng"
          },
          {
            "name": "于田",
            "code": "CN101131307",
            "name_en": "yutian"
          }
        ]
      },
      {
        "name": "阿勒泰",
        "county": [
          {
            "name": "阿勒泰",
            "code": "CN101131401",
            "name_en": "aletai"
          },
          {
            "name": "哈巴河",
            "code": "CN101131402",
            "name_en": "habahe"
          },
          {
            "name": "吉木乃",
            "code": "CN101131405",
            "name_en": "jimunai"
          },
          {
            "name": "布尔津",
            "code": "CN101131406",
            "name_en": "buerjin"
          },
          {
            "name": "福海",
            "code": "CN101131407",
            "name_en": "fuhai"
          },
          {
            "name": "富蕴",
            "code": "CN101131408",
            "name_en": "fuyun"
          },
          {
            "name": "青河",
            "code": "CN101131409",
            "name_en": "qinghe"
          }
        ]
      },
      {
        "name": "克州",
        "county": [
          {
            "name": "阿图什",
            "code": "CN101131501",
            "name_en": "atushi"
          },
          {
            "name": "乌恰",
            "code": "CN101131502",
            "name_en": "wuqia"
          },
          {
            "name": "阿克陶",
            "code": "CN101131503",
            "name_en": "aketao"
          },
          {
            "name": "阿合奇",
            "code": "CN101131504",
            "name_en": "aheqi"
          }
        ]
      },
      {
        "name": "博尔塔拉",
        "county": [
          {
            "name": "博乐",
            "code": "CN101131601",
            "name_en": "bole"
          },
          {
            "name": "温泉",
            "code": "CN101131602",
            "name_en": "wenquan"
          },
          {
            "name": "精河",
            "code": "CN101131603",
            "name_en": "jinghe"
          },
          {
            "name": "阿拉山口",
            "code": "CN101131606",
            "name_en": "alashankou"
          }
        ]
      }
    ]
  },
  {
    "name": "西藏",
    "name_en": "xizang",
    "city": [
      {
        "name": "拉萨",
        "county": [
          {
            "name": "拉萨",
            "code": "CN101140101",
            "name_en": "lasa"
          },
          {
            "name": "当雄",
            "code": "CN101140102",
            "name_en": "dangxiong"
          },
          {
            "name": "尼木",
            "code": "CN101140103",
            "name_en": "nimu"
          },
          {
            "name": "林周",
            "code": "CN101140104",
            "name_en": "linzhou"
          },
          {
            "name": "堆龙德庆",
            "code": "CN101140105",
            "name_en": "duilongdeqing"
          },
          {
            "name": "曲水",
            "code": "CN101140106",
            "name_en": "qushui"
          },
          {
            "name": "达孜",
            "code": "CN101140107",
            "name_en": "dazi"
          },
          {
            "name": "墨竹工卡",
            "code": "CN101140108",
            "name_en": "mozhugongka"
          }
        ]
      },
      {
        "name": "日喀则",
        "county": [
          {
            "name": "日喀则",
            "code": "CN101140201",
            "name_en": "rikaze"
          },
          {
            "name": "拉孜",
            "code": "CN101140202",
            "name_en": "lazi"
          },
          {
            "name": "南木林",
            "code": "CN101140203",
            "name_en": "nanmulin"
          },
          {
            "name": "聂拉木",
            "code": "CN101140204",
            "name_en": "nielamu"
          },
          {
            "name": "定日",
            "code": "CN101140205",
            "name_en": "anri"
          },
          {
            "name": "江孜",
            "code": "CN101140206",
            "name_en": "jiangzi"
          },
          {
            "name": "帕里",
            "code": "CN101140207",
            "name_en": "pali"
          },
          {
            "name": "仲巴",
            "code": "CN101140208",
            "name_en": "zhongba"
          },
          {
            "name": "萨嘎",
            "code": "CN101140209",
            "name_en": "saga"
          },
          {
            "name": "吉隆",
            "code": "CN101140210",
            "name_en": "jilong"
          },
          {
            "name": "昂仁",
            "code": "CN101140211",
            "name_en": "angren"
          },
          {
            "name": "定结",
            "code": "CN101140212",
            "name_en": "dingjie"
          },
          {
            "name": "萨迦",
            "code": "CN101140213",
            "name_en": "sajia"
          },
          {
            "name": "谢通门",
            "code": "CN101140214",
            "name_en": "xietongmen"
          },
          {
            "name": "岗巴",
            "code": "CN101140216",
            "name_en": "gangba"
          },
          {
            "name": "白朗",
            "code": "CN101140217",
            "name_en": "bailang"
          },
          {
            "name": "亚东",
            "code": "CN101140218",
            "name_en": "yadong"
          },
          {
            "name": "康马",
            "code": "CN101140219",
            "name_en": "kangma"
          },
          {
            "name": "仁布",
            "code": "CN101140220",
            "name_en": "renbu"
          }
        ]
      },
      {
        "name": "山南",
        "county": [
          {
            "name": "山南",
            "code": "CN101140301",
            "name_en": "shannan"
          },
          {
            "name": "贡嘎",
            "code": "CN101140302",
            "name_en": "gongga"
          },
          {
            "name": "札囊",
            "code": "CN101140303",
            "name_en": "zhanan"
          },
          {
            "name": "加查",
            "code": "CN101140304",
            "name_en": "jiacha"
          },
          {
            "name": "浪卡子",
            "code": "CN101140305",
            "name_en": "langkazi"
          },
          {
            "name": "错那",
            "code": "CN101140306",
            "name_en": "cuona"
          },
          {
            "name": "隆子",
            "code": "CN101140307",
            "name_en": "longzi"
          },
          {
            "name": "泽当",
            "code": "CN101140308",
            "name_en": "zedang"
          },
          {
            "name": "乃东",
            "code": "CN101140309",
            "name_en": "naidong"
          },
          {
            "name": "桑日",
            "code": "CN101140310",
            "name_en": "sangri"
          },
          {
            "name": "洛扎",
            "code": "CN101140311",
            "name_en": "luozha"
          },
          {
            "name": "措美",
            "code": "CN101140312",
            "name_en": "cuomei"
          },
          {
            "name": "琼结",
            "code": "CN101140313",
            "name_en": "qiongjie"
          },
          {
            "name": "曲松",
            "code": "CN101140314",
            "name_en": "qusong"
          }
        ]
      },
      {
        "name": "林芝",
        "county": [
          {
            "name": "林芝",
            "code": "CN101140401",
            "name_en": "linzhi"
          },
          {
            "name": "波密",
            "code": "CN101140402",
            "name_en": "bomi"
          },
          {
            "name": "米林",
            "code": "CN101140403",
            "name_en": "milin"
          },
          {
            "name": "察隅",
            "code": "CN101140404",
            "name_en": "chayu"
          },
          {
            "name": "工布江达",
            "code": "CN101140405",
            "name_en": "gongbujiangda"
          },
          {
            "name": "朗县",
            "code": "CN101140406",
            "name_en": "langxian"
          },
          {
            "name": "墨脱",
            "code": "CN101140407",
            "name_en": "motuo"
          }
        ]
      },
      {
        "name": "昌都",
        "county": [
          {
            "name": "昌都",
            "code": "CN101140501",
            "name_en": "changdu"
          },
          {
            "name": "丁青",
            "code": "CN101140502",
            "name_en": "dingqing"
          },
          {
            "name": "边坝",
            "code": "CN101140503",
            "name_en": "bianba"
          },
          {
            "name": "洛隆",
            "code": "CN101140504",
            "name_en": "luolong"
          },
          {
            "name": "左贡",
            "code": "CN101140505",
            "name_en": "zuogong"
          },
          {
            "name": "芒康",
            "code": "CN101140506",
            "name_en": "mangkang"
          },
          {
            "name": "类乌齐",
            "code": "CN101140507",
            "name_en": "leiwuqi"
          },
          {
            "name": "八宿",
            "code": "CN101140508",
            "name_en": "basu"
          },
          {
            "name": "江达",
            "code": "CN101140509",
            "name_en": "jiangda"
          },
          {
            "name": "察雅",
            "code": "CN101140510",
            "name_en": "chaya"
          },
          {
            "name": "贡觉",
            "code": "CN101140511",
            "name_en": "gongjue"
          }
        ]
      },
      {
        "name": "那曲",
        "county": [
          {
            "name": "那曲",
            "code": "CN101140601",
            "name_en": "naqu"
          },
          {
            "name": "尼玛",
            "code": "CN101140602",
            "name_en": "nima"
          },
          {
            "name": "嘉黎",
            "code": "CN101140603",
            "name_en": "jiali"
          },
          {
            "name": "班戈",
            "code": "CN101140604",
            "name_en": "bange"
          },
          {
            "name": "安多",
            "code": "CN101140605",
            "name_en": "anduo"
          },
          {
            "name": "索县",
            "code": "CN101140606",
            "name_en": "suoxian"
          },
          {
            "name": "聂荣",
            "code": "CN101140607",
            "name_en": "nierong"
          },
          {
            "name": "巴青",
            "code": "CN101140608",
            "name_en": "baqing"
          },
          {
            "name": "比如",
            "code": "CN101140609",
            "name_en": "biru"
          },
          {
            "name": "双湖",
            "code": "CN101140610",
            "name_en": "shuanghu"
          }
        ]
      },
      {
        "name": "阿里",
        "county": [
          {
            "name": "阿里",
            "code": "CN101140701",
            "name_en": "ali"
          },
          {
            "name": "改则",
            "code": "CN101140702",
            "name_en": "gaize"
          },
          {
            "name": "申扎",
            "code": "CN101140703",
            "name_en": "shenzha"
          },
          {
            "name": "狮泉河",
            "code": "CN101140704",
            "name_en": "shiquanhe"
          },
          {
            "name": "普兰",
            "code": "CN101140705",
            "name_en": "pulan"
          },
          {
            "name": "札达",
            "code": "CN101140706",
            "name_en": "zhada"
          },
          {
            "name": "噶尔",
            "code": "CN101140707",
            "name_en": "gaer"
          },
          {
            "name": "日土",
            "code": "CN101140708",
            "name_en": "ritu"
          },
          {
            "name": "革吉",
            "code": "CN101140709",
            "name_en": "geji"
          },
          {
            "name": "措勤",
            "code": "CN101140710",
            "name_en": "cuoqin"
          }
        ]
      }
    ]
  },
  {
    "name": "青海",
    "name_en": "qinghai",
    "city": [
      {
        "name": "西宁",
        "county": [
          {
            "name": "西宁",
            "code": "CN101150101",
            "name_en": "xining"
          },
          {
            "name": "大通",
            "code": "CN101150102",
            "name_en": "datong"
          },
          {
            "name": "湟源",
            "code": "CN101150103",
            "name_en": "huangyuan"
          },
          {
            "name": "湟中",
            "code": "CN101150104",
            "name_en": "huangzhong"
          }
        ]
      },
      {
        "name": "海东",
        "county": [
          {
            "name": "海东",
            "code": "CN101150201",
            "name_en": "haidong"
          },
          {
            "name": "乐都",
            "code": "CN101150202",
            "name_en": "ledu"
          },
          {
            "name": "民和",
            "code": "CN101150203",
            "name_en": "minhe"
          },
          {
            "name": "互助",
            "code": "CN101150204",
            "name_en": "huzhu"
          },
          {
            "name": "化隆",
            "code": "CN101150205",
            "name_en": "hualong"
          },
          {
            "name": "循化",
            "code": "CN101150206",
            "name_en": "xunhua"
          },
          {
            "name": "冷湖",
            "code": "CN101150207",
            "name_en": "lenghu"
          },
          {
            "name": "平安",
            "code": "CN101150208",
            "name_en": "pingan"
          }
        ]
      },
      {
        "name": "黄南",
        "county": [
          {
            "name": "黄南",
            "code": "CN101150301",
            "name_en": "huangnan"
          },
          {
            "name": "尖扎",
            "code": "CN101150302",
            "name_en": "jianzha"
          },
          {
            "name": "泽库",
            "code": "CN101150303",
            "name_en": "zeku"
          },
          {
            "name": "河南",
            "code": "CN101150304",
            "name_en": "henan"
          },
          {
            "name": "同仁",
            "code": "CN101150305",
            "name_en": "tongren"
          }
        ]
      },
      {
        "name": "海南",
        "county": [
          {
            "name": "海南",
            "code": "CN101150401",
            "name_en": "hainan"
          },
          {
            "name": "贵德",
            "code": "CN101150404",
            "name_en": "guide"
          },
          {
            "name": "兴海",
            "code": "CN101150406",
            "name_en": "xinghai"
          },
          {
            "name": "贵南",
            "code": "CN101150407",
            "name_en": "guinan"
          },
          {
            "name": "同德",
            "code": "CN101150408",
            "name_en": "tongde"
          },
          {
            "name": "共和",
            "code": "CN101150409",
            "name_en": "gonghe"
          }
        ]
      },
      {
        "name": "果洛",
        "county": [
          {
            "name": "果洛",
            "code": "CN101150501",
            "name_en": "guoluo"
          },
          {
            "name": "班玛",
            "code": "CN101150502",
            "name_en": "banma"
          },
          {
            "name": "甘德",
            "code": "CN101150503",
            "name_en": "gande"
          },
          {
            "name": "达日",
            "code": "CN101150504",
            "name_en": "dari"
          },
          {
            "name": "久治",
            "code": "CN101150505",
            "name_en": "jiuzhi"
          },
          {
            "name": "玛多",
            "code": "CN101150506",
            "name_en": "madu"
          },
          {
            "name": "玛沁",
            "code": "CN101150508",
            "name_en": "maqin"
          }
        ]
      },
      {
        "name": "玉树",
        "county": [
          {
            "name": "玉树",
            "code": "CN101150601",
            "name_en": "yushu"
          },
          {
            "name": "称多",
            "code": "CN101150602",
            "name_en": "chenduo"
          },
          {
            "name": "治多",
            "code": "CN101150603",
            "name_en": "zhiduo"
          },
          {
            "name": "杂多",
            "code": "CN101150604",
            "name_en": "zaduo"
          },
          {
            "name": "囊谦",
            "code": "CN101150605",
            "name_en": "nangqian"
          },
          {
            "name": "曲麻莱",
            "code": "CN101150606",
            "name_en": "qumacai"
          }
        ]
      },
      {
        "name": "海西",
        "county": [
          {
            "name": "海西",
            "code": "CN101150701",
            "name_en": "haixi"
          },
          {
            "name": "天峻",
            "code": "CN101150708",
            "name_en": "tianjun"
          },
          {
            "name": "乌兰",
            "code": "CN101150709",
            "name_en": "wulan"
          },
          {
            "name": "茫崖",
            "code": "CN101150712",
            "name_en": "mangai"
          },
          {
            "name": "大柴旦",
            "code": "CN101150713",
            "name_en": "dachaidan"
          },
          {
            "name": "德令哈",
            "code": "CN101150716",
            "name_en": "delingha"
          }
        ]
      },
      {
        "name": "海北",
        "county": [
          {
            "name": "海北",
            "code": "CN101150801",
            "name_en": "haibei"
          },
          {
            "name": "门源",
            "code": "CN101150802",
            "name_en": "menyuan"
          },
          {
            "name": "祁连",
            "code": "CN101150803",
            "name_en": "qilian"
          },
          {
            "name": "海晏",
            "code": "CN101150804",
            "name_en": "haiman"
          },
          {
            "name": "刚察",
            "code": "CN101150806",
            "name_en": "gangcha"
          }
        ]
      },
      {
        "name": "格尔木",
        "county": [
          {
            "name": "格尔木",
            "code": "CN101150901",
            "name_en": "geermu"
          },
          {
            "name": "都兰",
            "code": "CN101150902",
            "name_en": "dulan"
          }
        ]
      }
    ]
  },
  {
    "name": "甘肃",
    "name_en": "gansu",
    "city": [
      {
        "name": "兰州",
        "county": [
          {
            "name": "兰州",
            "code": "CN101160101",
            "name_en": "lanzhou"
          },
          {
            "name": "皋兰",
            "code": "CN101160102",
            "name_en": "gaolan"
          },
          {
            "name": "永登",
            "code": "CN101160103",
            "name_en": "yongdeng"
          },
          {
            "name": "榆中",
            "code": "CN101160104",
            "name_en": "yuzhong"
          }
        ]
      },
      {
        "name": "定西",
        "county": [
          {
            "name": "定西",
            "code": "CN101160201",
            "name_en": "dingxi"
          },
          {
            "name": "通渭",
            "code": "CN101160202",
            "name_en": "tongwei"
          },
          {
            "name": "陇西",
            "code": "CN101160203",
            "name_en": "longxi"
          },
          {
            "name": "渭源",
            "code": "CN101160204",
            "name_en": "weiyuan"
          },
          {
            "name": "临洮",
            "code": "CN101160205",
            "name_en": "lintao"
          },
          {
            "name": "漳县",
            "code": "CN101160206",
            "name_en": "zhangxian"
          },
          {
            "name": "岷县",
            "code": "CN101160207",
            "name_en": "minxian"
          },
          {
            "name": "安定",
            "code": "CN101160208",
            "name_en": "anding"
          }
        ]
      },
      {
        "name": "平凉",
        "county": [
          {
            "name": "平凉",
            "code": "CN101160301",
            "name_en": "pingliang"
          },
          {
            "name": "泾川",
            "code": "CN101160302",
            "name_en": "jingchuan"
          },
          {
            "name": "灵台",
            "code": "CN101160303",
            "name_en": "lingtai"
          },
          {
            "name": "崇信",
            "code": "CN101160304",
            "name_en": "chongxin"
          },
          {
            "name": "华亭",
            "code": "CN101160305",
            "name_en": "huating"
          },
          {
            "name": "庄浪",
            "code": "CN101160306",
            "name_en": "zhuanglang"
          },
          {
            "name": "静宁",
            "code": "CN101160307",
            "name_en": "jingning"
          },
          {
            "name": "崆峒",
            "code": "CN101160308",
            "name_en": "kongtong"
          }
        ]
      },
      {
        "name": "庆阳",
        "county": [
          {
            "name": "庆阳",
            "code": "CN101160401",
            "name_en": "qingyang"
          },
          {
            "name": "环县",
            "code": "CN101160403",
            "name_en": "huanxian"
          },
          {
            "name": "华池",
            "code": "CN101160404",
            "name_en": "huachi"
          },
          {
            "name": "合水",
            "code": "CN101160405",
            "name_en": "heshui"
          },
          {
            "name": "正宁",
            "code": "CN101160406",
            "name_en": "zhengning"
          },
          {
            "name": "宁县",
            "code": "CN101160407",
            "name_en": "ningxian"
          },
          {
            "name": "镇原",
            "code": "CN101160408",
            "name_en": "zhenyuan"
          },
          {
            "name": "庆城",
            "code": "CN101160409",
            "name_en": "qingcheng"
          }
        ]
      },
      {
        "name": "武威",
        "county": [
          {
            "name": "武威",
            "code": "CN101160501",
            "name_en": "wuwei"
          },
          {
            "name": "民勤",
            "code": "CN101160502",
            "name_en": "minqin"
          },
          {
            "name": "古浪",
            "code": "CN101160503",
            "name_en": "gulang"
          },
          {
            "name": "天祝",
            "code": "CN101160505",
            "name_en": "tianzhu"
          }
        ]
      },
      {
        "name": "金昌",
        "county": [
          {
            "name": "金昌",
            "code": "CN101160601",
            "name_en": "jinchang"
          },
          {
            "name": "永昌",
            "code": "CN101160602",
            "name_en": "yongchang"
          }
        ]
      },
      {
        "name": "张掖",
        "county": [
          {
            "name": "张掖",
            "code": "CN101160701",
            "name_en": "zhangye"
          },
          {
            "name": "肃南",
            "code": "CN101160702",
            "name_en": "sunan"
          },
          {
            "name": "民乐",
            "code": "CN101160703",
            "name_en": "minle"
          },
          {
            "name": "临泽",
            "code": "CN101160704",
            "name_en": "linze"
          },
          {
            "name": "高台",
            "code": "CN101160705",
            "name_en": "gaotai"
          },
          {
            "name": "山丹",
            "code": "CN101160706",
            "name_en": "shandan"
          }
        ]
      },
      {
        "name": "酒泉",
        "county": [
          {
            "name": "酒泉",
            "code": "CN101160801",
            "name_en": "jiuquan"
          },
          {
            "name": "金塔",
            "code": "CN101160803",
            "name_en": "jinta"
          },
          {
            "name": "阿克塞",
            "code": "CN101160804",
            "name_en": "akesai"
          },
          {
            "name": "瓜州",
            "code": "CN101160805",
            "name_en": "guazhou"
          },
          {
            "name": "肃北",
            "code": "CN101160806",
            "name_en": "subei"
          },
          {
            "name": "玉门",
            "code": "CN101160807",
            "name_en": "yumen"
          },
          {
            "name": "敦煌",
            "code": "CN101160808",
            "name_en": "dunhuang"
          }
        ]
      },
      {
        "name": "天水",
        "county": [
          {
            "name": "天水",
            "code": "CN101160901",
            "name_en": "tianshui"
          },
          {
            "name": "清水",
            "code": "CN101160903",
            "name_en": "qingshui"
          },
          {
            "name": "秦安",
            "code": "CN101160904",
            "name_en": "qinan"
          },
          {
            "name": "甘谷",
            "code": "CN101160905",
            "name_en": "gangu"
          },
          {
            "name": "武山",
            "code": "CN101160906",
            "name_en": "wushan"
          },
          {
            "name": "张家川",
            "code": "CN101160907",
            "name_en": "zhangjiachuan"
          },
          {
            "name": "麦积",
            "code": "CN101160908",
            "name_en": "maiji"
          }
        ]
      },
      {
        "name": "陇南",
        "county": [
          {
            "name": "武都",
            "code": "CN101161001",
            "name_en": "wudu"
          },
          {
            "name": "成县",
            "code": "CN101161002",
            "name_en": "chengxian"
          },
          {
            "name": "文县",
            "code": "CN101161003",
            "name_en": "wenxian"
          },
          {
            "name": "宕昌",
            "code": "CN101161004",
            "name_en": "dangchang"
          },
          {
            "name": "康县",
            "code": "CN101161005",
            "name_en": "kangxian"
          },
          {
            "name": "西和",
            "code": "CN101161006",
            "name_en": "xihe"
          },
          {
            "name": "礼县",
            "code": "CN101161007",
            "name_en": "lixian"
          },
          {
            "name": "徽县",
            "code": "CN101161008",
            "name_en": "huixian"
          },
          {
            "name": "两当",
            "code": "CN101161009",
            "name_en": "liangdang"
          }
        ]
      },
      {
        "name": "临夏",
        "county": [
          {
            "name": "临夏",
            "code": "CN101161101",
            "name_en": "linxia"
          },
          {
            "name": "康乐",
            "code": "CN101161102",
            "name_en": "kangle"
          },
          {
            "name": "永靖",
            "code": "CN101161103",
            "name_en": "yongjing"
          },
          {
            "name": "广河",
            "code": "CN101161104",
            "name_en": "guanghe"
          },
          {
            "name": "和政",
            "code": "CN101161105",
            "name_en": "hezheng"
          },
          {
            "name": "东乡",
            "code": "CN101161106",
            "name_en": "dongxiang"
          },
          {
            "name": "积石山",
            "code": "CN101161107",
            "name_en": "jishishan"
          }
        ]
      },
      {
        "name": "甘南",
        "county": [
          {
            "name": "合作",
            "code": "CN101161201",
            "name_en": "hezuo"
          },
          {
            "name": "临潭",
            "code": "CN101161202",
            "name_en": "lintan"
          },
          {
            "name": "卓尼",
            "code": "CN101161203",
            "name_en": "zhuoni"
          },
          {
            "name": "舟曲",
            "code": "CN101161204",
            "name_en": "zhouqu"
          },
          {
            "name": "迭部",
            "code": "CN101161205",
            "name_en": "diebu"
          },
          {
            "name": "玛曲",
            "code": "CN101161206",
            "name_en": "maqu"
          },
          {
            "name": "碌曲",
            "code": "CN101161207",
            "name_en": "luqu"
          },
          {
            "name": "夏河",
            "code": "CN101161208",
            "name_en": "xiahe"
          }
        ]
      },
      {
        "name": "白银",
        "county": [
          {
            "name": "白银",
            "code": "CN101161301",
            "name_en": "baiyin"
          },
          {
            "name": "靖远",
            "code": "CN101161302",
            "name_en": "jingyuan"
          },
          {
            "name": "会宁",
            "code": "CN101161303",
            "name_en": "huining"
          },
          {
            "name": "平川",
            "code": "CN101161304",
            "name_en": "pingchuan"
          },
          {
            "name": "景泰",
            "code": "CN101161305",
            "name_en": "jingtai"
          }
        ]
      },
      {
        "name": "嘉峪关",
        "county": [
          {
            "name": "嘉峪关",
            "code": "CN101161401",
            "name_en": "jiayuguan"
          }
        ]
      }
    ]
  },
  {
    "name": "宁夏",
    "name_en": "ningxia",
    "city": [
      {
        "name": "银川",
        "county": [
          {
            "name": "银川",
            "code": "CN101170101",
            "name_en": "yinchuan"
          },
          {
            "name": "永宁",
            "code": "CN101170102",
            "name_en": "yongning"
          },
          {
            "name": "灵武",
            "code": "CN101170103",
            "name_en": "lingwu"
          },
          {
            "name": "贺兰",
            "code": "CN101170104",
            "name_en": "helan"
          }
        ]
      },
      {
        "name": "石嘴山",
        "county": [
          {
            "name": "石嘴山",
            "code": "CN101170201",
            "name_en": "shizuishan"
          },
          {
            "name": "惠农",
            "code": "CN101170202",
            "name_en": "huinong"
          },
          {
            "name": "平罗",
            "code": "CN101170203",
            "name_en": "pingluo"
          },
          {
            "name": "陶乐",
            "code": "CN101170204",
            "name_en": "taole"
          }
        ]
      },
      {
        "name": "吴忠",
        "county": [
          {
            "name": "吴忠",
            "code": "CN101170301",
            "name_en": "wuzhong"
          },
          {
            "name": "同心",
            "code": "CN101170302",
            "name_en": "tongxin"
          },
          {
            "name": "盐池",
            "code": "CN101170303",
            "name_en": "yanchi"
          },
          {
            "name": "青铜峡",
            "code": "CN101170306",
            "name_en": "qingtongxia"
          }
        ]
      },
      {
        "name": "固原",
        "county": [
          {
            "name": "固原",
            "code": "CN101170401",
            "name_en": "guyuan"
          },
          {
            "name": "西吉",
            "code": "CN101170402",
            "name_en": "xiji"
          },
          {
            "name": "隆德",
            "code": "CN101170403",
            "name_en": "longde"
          },
          {
            "name": "泾源",
            "code": "CN101170404",
            "name_en": "jinyuan"
          },
          {
            "name": "彭阳",
            "code": "CN101170406",
            "name_en": "pengyang"
          }
        ]
      },
      {
        "name": "中卫",
        "county": [
          {
            "name": "中卫",
            "code": "CN101170501",
            "name_en": "zhongwei"
          },
          {
            "name": "中宁",
            "code": "CN101170502",
            "name_en": "zhongning"
          },
          {
            "name": "海原",
            "code": "CN101170504",
            "name_en": "haiyuan"
          }
        ]
      }
    ]
  },
  {
    "name": "河南",
    "name_en": "henan",
    "city": [
      {
        "name": "郑州",
        "county": [
          {
            "name": "郑州",
            "code": "CN101180101",
            "name_en": "zhengzhou"
          },
          {
            "name": "巩义",
            "code": "CN101180102",
            "name_en": "gongyi"
          },
          {
            "name": "荥阳",
            "code": "CN101180103",
            "name_en": "xingyang"
          },
          {
            "name": "登封",
            "code": "CN101180104",
            "name_en": "dengfeng"
          },
          {
            "name": "新密",
            "code": "CN101180105",
            "name_en": "xinmi"
          },
          {
            "name": "新郑",
            "code": "CN101180106",
            "name_en": "xinzheng"
          },
          {
            "name": "中牟",
            "code": "CN101180107",
            "name_en": "zhongmou"
          },
          {
            "name": "上街",
            "code": "CN101180108",
            "name_en": "shangjie"
          }
        ]
      },
      {
        "name": "安阳",
        "county": [
          {
            "name": "安阳",
            "code": "CN101180201",
            "name_en": "anyang"
          },
          {
            "name": "汤阴",
            "code": "CN101180202",
            "name_en": "tangyin"
          },
          {
            "name": "滑县",
            "code": "CN101180203",
            "name_en": "huaxian"
          },
          {
            "name": "内黄",
            "code": "CN101180204",
            "name_en": "neihuang"
          },
          {
            "name": "林州",
            "code": "CN101180205",
            "name_en": "linzhou"
          }
        ]
      },
      {
        "name": "新乡",
        "county": [
          {
            "name": "新乡",
            "code": "CN101180301",
            "name_en": "xinxiang"
          },
          {
            "name": "获嘉",
            "code": "CN101180302",
            "name_en": "huojia"
          },
          {
            "name": "原阳",
            "code": "CN101180303",
            "name_en": "yuanyang"
          },
          {
            "name": "辉县",
            "code": "CN101180304",
            "name_en": "huixian"
          },
          {
            "name": "卫辉",
            "code": "CN101180305",
            "name_en": "weihui"
          },
          {
            "name": "延津",
            "code": "CN101180306",
            "name_en": "yanjin"
          },
          {
            "name": "封丘",
            "code": "CN101180307",
            "name_en": "fengqiu"
          },
          {
            "name": "长垣",
            "code": "CN101180308",
            "name_en": "changyuan"
          }
        ]
      },
      {
        "name": "许昌",
        "county": [
          {
            "name": "许昌",
            "code": "CN101180401",
            "name_en": "xuchang"
          },
          {
            "name": "鄢陵",
            "code": "CN101180402",
            "name_en": "yanling"
          },
          {
            "name": "襄城",
            "code": "CN101180403",
            "name_en": "xiangcheng"
          },
          {
            "name": "长葛",
            "code": "CN101180404",
            "name_en": "changge"
          },
          {
            "name": "禹州",
            "code": "CN101180405",
            "name_en": "yuzhou"
          }
        ]
      },
      {
        "name": "平顶山",
        "county": [
          {
            "name": "平顶山",
            "code": "CN101180501",
            "name_en": "pingdingshan"
          },
          {
            "name": "郏县",
            "code": "CN101180502",
            "name_en": "jiaxian"
          },
          {
            "name": "宝丰",
            "code": "CN101180503",
            "name_en": "baofeng"
          },
          {
            "name": "汝州",
            "code": "CN101180504",
            "name_en": "ruzhou"
          },
          {
            "name": "叶县",
            "code": "CN101180505",
            "name_en": "yexian"
          },
          {
            "name": "舞钢",
            "code": "CN101180506",
            "name_en": "wugang"
          },
          {
            "name": "鲁山",
            "code": "CN101180507",
            "name_en": "lushan"
          },
          {
            "name": "石龙",
            "code": "CN101180508",
            "name_en": "shilong"
          }
        ]
      },
      {
        "name": "信阳",
        "county": [
          {
            "name": "信阳",
            "code": "CN101180601",
            "name_en": "xinyang"
          },
          {
            "name": "息县",
            "code": "CN101180602",
            "name_en": "xixian"
          },
          {
            "name": "罗山",
            "code": "CN101180603",
            "name_en": "luoshan"
          },
          {
            "name": "光山",
            "code": "CN101180604",
            "name_en": "guangshan"
          },
          {
            "name": "新县",
            "code": "CN101180605",
            "name_en": "xinxian"
          },
          {
            "name": "淮滨",
            "code": "CN101180606",
            "name_en": "huaibin"
          },
          {
            "name": "潢川",
            "code": "CN101180607",
            "name_en": "huangchuan"
          },
          {
            "name": "固始",
            "code": "CN101180608",
            "name_en": "gushi"
          },
          {
            "name": "商城",
            "code": "CN101180609",
            "name_en": "shangcheng"
          }
        ]
      },
      {
        "name": "南阳",
        "county": [
          {
            "name": "南阳",
            "code": "CN101180701",
            "name_en": "nanyang"
          },
          {
            "name": "南召",
            "code": "CN101180702",
            "name_en": "nanzhao"
          },
          {
            "name": "方城",
            "code": "CN101180703",
            "name_en": "fangcheng"
          },
          {
            "name": "社旗",
            "code": "CN101180704",
            "name_en": "sheqi"
          },
          {
            "name": "西峡",
            "code": "CN101180705",
            "name_en": "xixia"
          },
          {
            "name": "内乡",
            "code": "CN101180706",
            "name_en": "neixiang"
          },
          {
            "name": "镇平",
            "code": "CN101180707",
            "name_en": "zhenping"
          },
          {
            "name": "淅川",
            "code": "CN101180708",
            "name_en": "xichuan"
          },
          {
            "name": "新野",
            "code": "CN101180709",
            "name_en": "xinye"
          },
          {
            "name": "唐河",
            "code": "CN101180710",
            "name_en": "tanghe"
          },
          {
            "name": "邓州",
            "code": "CN101180711",
            "name_en": "dengzhou"
          },
          {
            "name": "桐柏",
            "code": "CN101180712",
            "name_en": "tongbai"
          }
        ]
      },
      {
        "name": "开封",
        "county": [
          {
            "name": "开封",
            "code": "CN101180801",
            "name_en": "kaifeng"
          },
          {
            "name": "杞县",
            "code": "CN101180802",
            "name_en": "qixian"
          },
          {
            "name": "尉氏",
            "code": "CN101180803",
            "name_en": "weishi"
          },
          {
            "name": "通许",
            "code": "CN101180804",
            "name_en": "tongxu"
          },
          {
            "name": "兰考",
            "code": "CN101180805",
            "name_en": "lankao"
          }
        ]
      },
      {
        "name": "洛阳",
        "county": [
          {
            "name": "洛阳",
            "code": "CN101180901",
            "name_en": "luoyang"
          },
          {
            "name": "新安",
            "code": "CN101180902",
            "name_en": "xinan"
          },
          {
            "name": "孟津",
            "code": "CN101180903",
            "name_en": "mengjin"
          },
          {
            "name": "宜阳",
            "code": "CN101180904",
            "name_en": "yiyang"
          },
          {
            "name": "洛宁",
            "code": "CN101180905",
            "name_en": "luoning"
          },
          {
            "name": "伊川",
            "code": "CN101180906",
            "name_en": "yichuan"
          },
          {
            "name": "嵩县",
            "code": "CN101180907",
            "name_en": "songxian"
          },
          {
            "name": "偃师",
            "code": "CN101180908",
            "name_en": "yanshi"
          },
          {
            "name": "栾川",
            "code": "CN101180909",
            "name_en": "luanchuan"
          },
          {
            "name": "汝阳",
            "code": "CN101180910",
            "name_en": "ruyang"
          },
          {
            "name": "吉利",
            "code": "CN101180911",
            "name_en": "jili"
          }
        ]
      },
      {
        "name": "商丘",
        "county": [
          {
            "name": "商丘",
            "code": "CN101181001",
            "name_en": "shangqiu"
          },
          {
            "name": "睢县",
            "code": "CN101181003",
            "name_en": "suixian"
          },
          {
            "name": "民权",
            "code": "CN101181004",
            "name_en": "minquan"
          },
          {
            "name": "虞城",
            "code": "CN101181005",
            "name_en": "yucheng"
          },
          {
            "name": "柘城",
            "code": "CN101181006",
            "name_en": "zhecheng"
          },
          {
            "name": "宁陵",
            "code": "CN101181007",
            "name_en": "ningling"
          },
          {
            "name": "夏邑",
            "code": "CN101181008",
            "name_en": "xiayi"
          },
          {
            "name": "永城",
            "code": "CN101181009",
            "name_en": "yongcheng"
          }
        ]
      },
      {
        "name": "焦作",
        "county": [
          {
            "name": "焦作",
            "code": "CN101181101",
            "name_en": "jiaozuo"
          },
          {
            "name": "修武",
            "code": "CN101181102",
            "name_en": "xiuwu"
          },
          {
            "name": "武陟",
            "code": "CN101181103",
            "name_en": "wuzhi"
          },
          {
            "name": "沁阳",
            "code": "CN101181104",
            "name_en": "qinyang"
          },
          {
            "name": "博爱",
            "code": "CN101181106",
            "name_en": "boai"
          },
          {
            "name": "温县",
            "code": "CN101181107",
            "name_en": "wenxian"
          },
          {
            "name": "孟州",
            "code": "CN101181108",
            "name_en": "mengzhou"
          }
        ]
      },
      {
        "name": "鹤壁",
        "county": [
          {
            "name": "鹤壁",
            "code": "CN101181201",
            "name_en": "hebi"
          },
          {
            "name": "浚县",
            "code": "CN101181202",
            "name_en": "xunxian"
          },
          {
            "name": "淇县",
            "code": "CN101181203",
            "name_en": "qixian"
          }
        ]
      },
      {
        "name": "濮阳",
        "county": [
          {
            "name": "濮阳",
            "code": "CN101181301",
            "name_en": "puyang"
          },
          {
            "name": "台前",
            "code": "CN101181302",
            "name_en": "taiqian"
          },
          {
            "name": "南乐",
            "code": "CN101181303",
            "name_en": "nanle"
          },
          {
            "name": "清丰",
            "code": "CN101181304",
            "name_en": "qingfeng"
          },
          {
            "name": "范县",
            "code": "CN101181305",
            "name_en": "fanxian"
          }
        ]
      },
      {
        "name": "周口",
        "county": [
          {
            "name": "周口",
            "code": "CN101181401",
            "name_en": "zhoukou"
          },
          {
            "name": "扶沟",
            "code": "CN101181402",
            "name_en": "fugou"
          },
          {
            "name": "太康",
            "code": "CN101181403",
            "name_en": "taikang"
          },
          {
            "name": "淮阳",
            "code": "CN101181404",
            "name_en": "huaiyang"
          },
          {
            "name": "西华",
            "code": "CN101181405",
            "name_en": "xihua"
          },
          {
            "name": "商水",
            "code": "CN101181406",
            "name_en": "shangshui"
          },
          {
            "name": "项城",
            "code": "CN101181407",
            "name_en": "xiangcheng"
          },
          {
            "name": "郸城",
            "code": "CN101181408",
            "name_en": "dancheng"
          },
          {
            "name": "鹿邑",
            "code": "CN101181409",
            "name_en": "luyi"
          },
          {
            "name": "沈丘",
            "code": "CN101181410",
            "name_en": "shenqiu"
          }
        ]
      },
      {
        "name": "漯河",
        "county": [
          {
            "name": "漯河",
            "code": "CN101181501",
            "name_en": "luohe"
          },
          {
            "name": "临颍",
            "code": "CN101181502",
            "name_en": "linying"
          },
          {
            "name": "舞阳",
            "code": "CN101181503",
            "name_en": "wuyang"
          }
        ]
      },
      {
        "name": "驻马店",
        "county": [
          {
            "name": "驻马店",
            "code": "CN101181601",
            "name_en": "zhumadian"
          },
          {
            "name": "西平",
            "code": "CN101181602",
            "name_en": "xiping"
          },
          {
            "name": "遂平",
            "code": "CN101181603",
            "name_en": "suiping"
          },
          {
            "name": "上蔡",
            "code": "CN101181604",
            "name_en": "shangcai"
          },
          {
            "name": "汝南",
            "code": "CN101181605",
            "name_en": "runan"
          },
          {
            "name": "泌阳",
            "code": "CN101181606",
            "name_en": "biyang"
          },
          {
            "name": "平舆",
            "code": "CN101181607",
            "name_en": "pingyu"
          },
          {
            "name": "新蔡",
            "code": "CN101181608",
            "name_en": "xincai"
          },
          {
            "name": "确山",
            "code": "CN101181609",
            "name_en": "queshan"
          },
          {
            "name": "正阳",
            "code": "CN101181610",
            "name_en": "zhengyang"
          }
        ]
      },
      {
        "name": "三门峡",
        "county": [
          {
            "name": "三门峡",
            "code": "CN101181701",
            "name_en": "sanmenxia"
          },
          {
            "name": "灵宝",
            "code": "CN101181702",
            "name_en": "lingbao"
          },
          {
            "name": "渑池",
            "code": "CN101181703",
            "name_en": "mianchi"
          },
          {
            "name": "卢氏",
            "code": "CN101181704",
            "name_en": "lushi"
          },
          {
            "name": "义马",
            "code": "CN101181705",
            "name_en": "yima"
          },
          {
            "name": "陕县",
            "code": "CN101181706",
            "name_en": "shanxian"
          }
        ]
      },
      {
        "name": "济源",
        "county": [
          {
            "name": "济源",
            "code": "CN101181801",
            "name_en": "jiyuan"
          }
        ]
      }
    ]
  },
  {
    "name": "江苏",
    "name_en": "jiangsu",
    "city": [
      {
        "name": "南京",
        "county": [
          {
            "name": "南京",
            "code": "CN101190101",
            "name_en": "nanjing"
          },
          {
            "name": "溧水",
            "code": "CN101190102",
            "name_en": "lishui"
          },
          {
            "name": "高淳",
            "code": "CN101190103",
            "name_en": "gaochun"
          },
          {
            "name": "江宁",
            "code": "CN101190104",
            "name_en": "jiangning"
          },
          {
            "name": "六合",
            "code": "CN101190105",
            "name_en": "luhe"
          },
          {
            "name": "江浦",
            "code": "CN101190106",
            "name_en": "jiangpu"
          },
          {
            "name": "浦口",
            "code": "CN101190107",
            "name_en": "pukou"
          }
        ]
      },
      {
        "name": "无锡",
        "county": [
          {
            "name": "无锡",
            "code": "CN101190201",
            "name_en": "wuxi"
          },
          {
            "name": "江阴",
            "code": "CN101190202",
            "name_en": "jiangyin"
          },
          {
            "name": "宜兴",
            "code": "CN101190203",
            "name_en": "yixing"
          },
          {
            "name": "锡山",
            "code": "CN101190204",
            "name_en": "xishan"
          }
        ]
      },
      {
        "name": "镇江",
        "county": [
          {
            "name": "镇江",
            "code": "CN101190301",
            "name_en": "zhenjiang"
          },
          {
            "name": "丹阳",
            "code": "CN101190302",
            "name_en": "danyang"
          },
          {
            "name": "扬中",
            "code": "CN101190303",
            "name_en": "yangzhong"
          },
          {
            "name": "句容",
            "code": "CN101190304",
            "name_en": "jurong"
          },
          {
            "name": "丹徒",
            "code": "CN101190305",
            "name_en": "dantu"
          }
        ]
      },
      {
        "name": "苏州",
        "county": [
          {
            "name": "苏州",
            "code": "CN101190401",
            "name_en": "suzhou"
          },
          {
            "name": "常熟",
            "code": "CN101190402",
            "name_en": "changshu"
          },
          {
            "name": "张家港",
            "code": "CN101190403",
            "name_en": "zhangjiagang"
          },
          {
            "name": "昆山",
            "code": "CN101190404",
            "name_en": "kunshan"
          },
          {
            "name": "吴中",
            "code": "CN101190405",
            "name_en": "wuzhong"
          },
          {
            "name": "吴江",
            "code": "CN101190407",
            "name_en": "wujiang"
          },
          {
            "name": "太仓",
            "code": "CN101190408",
            "name_en": "taicang"
          }
        ]
      },
      {
        "name": "南通",
        "county": [
          {
            "name": "南通",
            "code": "CN101190501",
            "name_en": "nantong"
          },
          {
            "name": "海安",
            "code": "CN101190502",
            "name_en": "haian"
          },
          {
            "name": "如皋",
            "code": "CN101190503",
            "name_en": "rugao"
          },
          {
            "name": "如东",
            "code": "CN101190504",
            "name_en": "rudong"
          },
          {
            "name": "启东",
            "code": "CN101190507",
            "name_en": "qidong"
          },
          {
            "name": "海门",
            "code": "CN101190508",
            "name_en": "haimen"
          },
          {
            "name": "通州",
            "code": "CN101190509",
            "name_en": "tongzhou"
          }
        ]
      },
      {
        "name": "扬州",
        "county": [
          {
            "name": "扬州",
            "code": "CN101190601",
            "name_en": "yangzhou"
          },
          {
            "name": "宝应",
            "code": "CN101190602",
            "name_en": "baoying"
          },
          {
            "name": "仪征",
            "code": "CN101190603",
            "name_en": "yizheng"
          },
          {
            "name": "高邮",
            "code": "CN101190604",
            "name_en": "gaoyou"
          },
          {
            "name": "江都",
            "code": "CN101190605",
            "name_en": "jiangdu"
          },
          {
            "name": "邗江",
            "code": "CN101190606",
            "name_en": "hanjiang"
          }
        ]
      },
      {
        "name": "盐城",
        "county": [
          {
            "name": "盐城",
            "code": "CN101190701",
            "name_en": "yancheng"
          },
          {
            "name": "响水",
            "code": "CN101190702",
            "name_en": "xiangshui"
          },
          {
            "name": "滨海",
            "code": "CN101190703",
            "name_en": "binhai"
          },
          {
            "name": "阜宁",
            "code": "CN101190704",
            "name_en": "funing"
          },
          {
            "name": "射阳",
            "code": "CN101190705",
            "name_en": "sheyang"
          },
          {
            "name": "建湖",
            "code": "CN101190706",
            "name_en": "jianhu"
          },
          {
            "name": "东台",
            "code": "CN101190707",
            "name_en": "dongtai"
          },
          {
            "name": "大丰",
            "code": "CN101190708",
            "name_en": "dafeng"
          },
          {
            "name": "盐都",
            "code": "CN101190709",
            "name_en": "yandu"
          }
        ]
      },
      {
        "name": "徐州",
        "county": [
          {
            "name": "徐州",
            "code": "CN101190801",
            "name_en": "xuzhou"
          },
          {
            "name": "铜山",
            "code": "CN101190802",
            "name_en": "tongshan"
          },
          {
            "name": "丰县",
            "code": "CN101190803",
            "name_en": "fengxian"
          },
          {
            "name": "沛县",
            "code": "CN101190804",
            "name_en": "peixian"
          },
          {
            "name": "邳州",
            "code": "CN101190805",
            "name_en": "pizhou"
          },
          {
            "name": "睢宁",
            "code": "CN101190806",
            "name_en": "suining"
          },
          {
            "name": "新沂",
            "code": "CN101190807",
            "name_en": "xinyi"
          }
        ]
      },
      {
        "name": "淮安",
        "county": [
          {
            "name": "淮安",
            "code": "CN101190901",
            "name_en": "huaian"
          },
          {
            "name": "金湖",
            "code": "CN101190902",
            "name_en": "jinhu"
          },
          {
            "name": "盱眙",
            "code": "CN101190903",
            "name_en": "xuyi"
          },
          {
            "name": "洪泽",
            "code": "CN101190904",
            "name_en": "hongze"
          },
          {
            "name": "涟水",
            "code": "CN101190905",
            "name_en": "lianshui"
          },
          {
            "name": "淮阴区",
            "code": "CN101190906",
            "name_en": "huaiyinqu"
          },
          {
            "name": "淮安区",
            "code": "CN101190908",
            "name_en": "huaianqu"
          }
        ]
      },
      {
        "name": "连云港",
        "county": [
          {
            "name": "连云港",
            "code": "CN101191001",
            "name_en": "lianyungang"
          },
          {
            "name": "东海",
            "code": "CN101191002",
            "name_en": "donghai"
          },
          {
            "name": "赣榆",
            "code": "CN101191003",
            "name_en": "ganyu"
          },
          {
            "name": "灌云",
            "code": "CN101191004",
            "name_en": "guanyun"
          },
          {
            "name": "灌南",
            "code": "CN101191005",
            "name_en": "guannan"
          }
        ]
      },
      {
        "name": "常州",
        "county": [
          {
            "name": "常州",
            "code": "CN101191101",
            "name_en": "changzhou"
          },
          {
            "name": "溧阳",
            "code": "CN101191102",
            "name_en": "liyang"
          },
          {
            "name": "金坛",
            "code": "CN101191103",
            "name_en": "jintan"
          },
          {
            "name": "武进",
            "code": "CN101191104",
            "name_en": "wujin"
          }
        ]
      },
      {
        "name": "泰州",
        "county": [
          {
            "name": "泰州",
            "code": "CN101191201",
            "name_en": "taizhou"
          },
          {
            "name": "兴化",
            "code": "CN101191202",
            "name_en": "xinghua"
          },
          {
            "name": "泰兴",
            "code": "CN101191203",
            "name_en": "taixing"
          },
          {
            "name": "姜堰",
            "code": "CN101191204",
            "name_en": "jiangyan"
          },
          {
            "name": "靖江",
            "code": "CN101191205",
            "name_en": "jingjiang"
          }
        ]
      },
      {
        "name": "宿迁",
        "county": [
          {
            "name": "宿迁",
            "code": "CN101191301",
            "name_en": "suqian"
          },
          {
            "name": "沭阳",
            "code": "CN101191302",
            "name_en": "shuyang"
          },
          {
            "name": "泗阳",
            "code": "CN101191303",
            "name_en": "siyang"
          },
          {
            "name": "泗洪",
            "code": "CN101191304",
            "name_en": "sihong"
          },
          {
            "name": "宿豫",
            "code": "CN101191305",
            "name_en": "suyu"
          }
        ]
      }
    ]
  },
  {
    "name": "湖北",
    "name_en": "hubei",
    "city": [
      {
        "name": "武汉",
        "county": [
          {
            "name": "武汉",
            "code": "CN101200101",
            "name_en": "wuhan"
          },
          {
            "name": "蔡甸",
            "code": "CN101200102",
            "name_en": "caidian"
          },
          {
            "name": "黄陂",
            "code": "CN101200103",
            "name_en": "huangpi"
          },
          {
            "name": "新洲",
            "code": "CN101200104",
            "name_en": "xinzhou"
          },
          {
            "name": "江夏",
            "code": "CN101200105",
            "name_en": "jiangxia"
          },
          {
            "name": "东西湖",
            "code": "CN101200106",
            "name_en": "dongxihu"
          }
        ]
      },
      {
        "name": "襄阳",
        "county": [
          {
            "name": "襄阳",
            "code": "CN101200201",
            "name_en": "xiangyang"
          },
          {
            "name": "襄州",
            "code": "CN101200202",
            "name_en": "xiangzhou"
          },
          {
            "name": "保康",
            "code": "CN101200203",
            "name_en": "baokang"
          },
          {
            "name": "南漳",
            "code": "CN101200204",
            "name_en": "nanzhang"
          },
          {
            "name": "宜城",
            "code": "CN101200205",
            "name_en": "yicheng"
          },
          {
            "name": "老河口",
            "code": "CN101200206",
            "name_en": "laohekou"
          },
          {
            "name": "谷城",
            "code": "CN101200207",
            "name_en": "gucheng"
          },
          {
            "name": "枣阳",
            "code": "CN101200208",
            "name_en": "zaoyang"
          }
        ]
      },
      {
        "name": "鄂州",
        "county": [
          {
            "name": "鄂州",
            "code": "CN101200301",
            "name_en": "ezhou"
          },
          {
            "name": "梁子湖",
            "code": "CN101200302",
            "name_en": "liangzihu"
          }
        ]
      },
      {
        "name": "孝感",
        "county": [
          {
            "name": "孝感",
            "code": "CN101200401",
            "name_en": "xiaogan"
          },
          {
            "name": "安陆",
            "code": "CN101200402",
            "name_en": "anlu"
          },
          {
            "name": "云梦",
            "code": "CN101200403",
            "name_en": "yunmeng"
          },
          {
            "name": "大悟",
            "code": "CN101200404",
            "name_en": "dawu"
          },
          {
            "name": "应城",
            "code": "CN101200405",
            "name_en": "yingcheng"
          },
          {
            "name": "汉川",
            "code": "CN101200406",
            "name_en": "hanchuan"
          },
          {
            "name": "孝昌",
            "code": "CN101200407",
            "name_en": "xiaochang"
          }
        ]
      },
      {
        "name": "黄冈",
        "county": [
          {
            "name": "黄冈",
            "code": "CN101200501",
            "name_en": "huanggang"
          },
          {
            "name": "红安",
            "code": "CN101200502",
            "name_en": "hongan"
          },
          {
            "name": "麻城",
            "code": "CN101200503",
            "name_en": "macheng"
          },
          {
            "name": "罗田",
            "code": "CN101200504",
            "name_en": "luotian"
          },
          {
            "name": "英山",
            "code": "CN101200505",
            "name_en": "yingshan"
          },
          {
            "name": "浠水",
            "code": "CN101200506",
            "name_en": "xishui"
          },
          {
            "name": "蕲春",
            "code": "CN101200507",
            "name_en": "qichun"
          },
          {
            "name": "黄梅",
            "code": "CN101200508",
            "name_en": "huangmei"
          },
          {
            "name": "武穴",
            "code": "CN101200509",
            "name_en": "wuxue"
          },
          {
            "name": "团风",
            "code": "CN101200510",
            "name_en": "tuanfeng"
          }
        ]
      },
      {
        "name": "黄石",
        "county": [
          {
            "name": "黄石",
            "code": "CN101200601",
            "name_en": "huangshi"
          },
          {
            "name": "大冶",
            "code": "CN101200602",
            "name_en": "daye"
          },
          {
            "name": "阳新",
            "code": "CN101200603",
            "name_en": "yangxin"
          },
          {
            "name": "铁山",
            "code": "CN101200604",
            "name_en": "tieshan"
          },
          {
            "name": "下陆",
            "code": "CN101200605",
            "name_en": "xialu"
          },
          {
            "name": "西塞山",
            "code": "CN101200606",
            "name_en": "xisaishan"
          }
        ]
      },
      {
        "name": "咸宁",
        "county": [
          {
            "name": "咸宁",
            "code": "CN101200701",
            "name_en": "xianning"
          },
          {
            "name": "赤壁",
            "code": "CN101200702",
            "name_en": "chibi"
          },
          {
            "name": "嘉鱼",
            "code": "CN101200703",
            "name_en": "jiayu"
          },
          {
            "name": "崇阳",
            "code": "CN101200704",
            "name_en": "chongyang"
          },
          {
            "name": "通城",
            "code": "CN101200705",
            "name_en": "tongcheng"
          },
          {
            "name": "通山",
            "code": "CN101200706",
            "name_en": "tongshan"
          }
        ]
      },
      {
        "name": "荆州",
        "county": [
          {
            "name": "荆州",
            "code": "CN101200801",
            "name_en": "jingzhou"
          },
          {
            "name": "江陵",
            "code": "CN101200802",
            "name_en": "jiangling"
          },
          {
            "name": "公安",
            "code": "CN101200803",
            "name_en": "gongan"
          },
          {
            "name": "石首",
            "code": "CN101200804",
            "name_en": "shishou"
          },
          {
            "name": "监利",
            "code": "CN101200805",
            "name_en": "jianli"
          },
          {
            "name": "洪湖",
            "code": "CN101200806",
            "name_en": "honghu"
          },
          {
            "name": "松滋",
            "code": "CN101200807",
            "name_en": "songzi"
          }
        ]
      },
      {
        "name": "宜昌",
        "county": [
          {
            "name": "宜昌",
            "code": "CN101200901",
            "name_en": "yichang"
          },
          {
            "name": "远安",
            "code": "CN101200902",
            "name_en": "yuanan"
          },
          {
            "name": "秭归",
            "code": "CN101200903",
            "name_en": "zigui"
          },
          {
            "name": "兴山",
            "code": "CN101200904",
            "name_en": "xingshan"
          },
          {
            "name": "五峰",
            "code": "CN101200906",
            "name_en": "wufeng"
          },
          {
            "name": "当阳",
            "code": "CN101200907",
            "name_en": "dangyang"
          },
          {
            "name": "长阳",
            "code": "CN101200908",
            "name_en": "changyang"
          },
          {
            "name": "宜都",
            "code": "CN101200909",
            "name_en": "yidu"
          },
          {
            "name": "枝江",
            "code": "CN101200910",
            "name_en": "zhijiang"
          },
          {
            "name": "三峡",
            "code": "CN101200911",
            "name_en": "sanxia"
          },
          {
            "name": "夷陵",
            "code": "CN101200912",
            "name_en": "yiling"
          }
        ]
      },
      {
        "name": "恩施",
        "county": [
          {
            "name": "恩施",
            "code": "CN101201001",
            "name_en": "enshi"
          },
          {
            "name": "利川",
            "code": "CN101201002",
            "name_en": "lichuan"
          },
          {
            "name": "建始",
            "code": "CN101201003",
            "name_en": "jianshi"
          },
          {
            "name": "咸丰",
            "code": "CN101201004",
            "name_en": "xianfeng"
          },
          {
            "name": "宣恩",
            "code": "CN101201005",
            "name_en": "xuanen"
          },
          {
            "name": "鹤峰",
            "code": "CN101201006",
            "name_en": "hefeng"
          },
          {
            "name": "来凤",
            "code": "CN101201007",
            "name_en": "laifeng"
          },
          {
            "name": "巴东",
            "code": "CN101201008",
            "name_en": "badong"
          }
        ]
      },
      {
        "name": "十堰",
        "county": [
          {
            "name": "十堰",
            "code": "CN101201101",
            "name_en": "shiyan"
          },
          {
            "name": "竹溪",
            "code": "CN101201102",
            "name_en": "zhuxi"
          },
          {
            "name": "郧西",
            "code": "CN101201103",
            "name_en": "yunxi"
          },
          {
            "name": "郧县",
            "code": "CN101201104",
            "name_en": "yunxian"
          },
          {
            "name": "竹山",
            "code": "CN101201105",
            "name_en": "zhushan"
          },
          {
            "name": "房县",
            "code": "CN101201106",
            "name_en": "fangxian"
          },
          {
            "name": "丹江口",
            "code": "CN101201107",
            "name_en": "danjiangkou"
          },
          {
            "name": "茅箭",
            "code": "CN101201108",
            "name_en": "maojian"
          },
          {
            "name": "张湾",
            "code": "CN101201109",
            "name_en": "zhangwan"
          }
        ]
      },
      {
        "name": "神农架",
        "county": [
          {
            "name": "神农架",
            "code": "CN101201201",
            "name_en": "shennongjia"
          }
        ]
      },
      {
        "name": "随州",
        "county": [
          {
            "name": "随州",
            "code": "CN101201301",
            "name_en": "suizhou"
          },
          {
            "name": "广水",
            "code": "CN101201302",
            "name_en": "guangshui"
          }
        ]
      },
      {
        "name": "荆门",
        "county": [
          {
            "name": "荆门",
            "code": "CN101201401",
            "name_en": "jingmen"
          },
          {
            "name": "钟祥",
            "code": "CN101201402",
            "name_en": "zhongxiang"
          },
          {
            "name": "京山",
            "code": "CN101201403",
            "name_en": "jingshan"
          },
          {
            "name": "掇刀",
            "code": "CN101201404",
            "name_en": "duodao"
          },
          {
            "name": "沙洋",
            "code": "CN101201405",
            "name_en": "shayang"
          }
        ]
      },
      {
        "name": "荆州",
        "county": [
          {
            "name": "沙市",
            "code": "CN101201406",
            "name_en": "shashi"
          }
        ]
      },
      {
        "name": "天门",
        "county": [
          {
            "name": "天门",
            "code": "CN101201501",
            "name_en": "tianmen"
          }
        ]
      },
      {
        "name": "仙桃",
        "county": [
          {
            "name": "仙桃",
            "code": "CN101201601",
            "name_en": "xiantao"
          }
        ]
      },
      {
        "name": "潜江",
        "county": [
          {
            "name": "潜江",
            "code": "CN101201701",
            "name_en": "qianjiang"
          }
        ]
      }
    ]
  },
  {
    "name": "浙江",
    "name_en": "zhejiang",
    "city": [
      {
        "name": "杭州",
        "county": [
          {
            "name": "杭州",
            "code": "CN101210101",
            "name_en": "hangzhou"
          },
          {
            "name": "萧山",
            "code": "CN101210102",
            "name_en": "xiaoshan"
          },
          {
            "name": "桐庐",
            "code": "CN101210103",
            "name_en": "tonglu"
          },
          {
            "name": "淳安",
            "code": "CN101210104",
            "name_en": "chunan"
          },
          {
            "name": "建德",
            "code": "CN101210105",
            "name_en": "jiande"
          },
          {
            "name": "余杭",
            "code": "CN101210106",
            "name_en": "yuhang"
          },
          {
            "name": "临安",
            "code": "CN101210107",
            "name_en": "linan"
          },
          {
            "name": "富阳",
            "code": "CN101210108",
            "name_en": "fuyang"
          }
        ]
      },
      {
        "name": "湖州",
        "county": [
          {
            "name": "湖州",
            "code": "CN101210201",
            "name_en": "huzhou"
          },
          {
            "name": "长兴",
            "code": "CN101210202",
            "name_en": "changxing"
          },
          {
            "name": "安吉",
            "code": "CN101210203",
            "name_en": "anji"
          },
          {
            "name": "德清",
            "code": "CN101210204",
            "name_en": "deqing"
          }
        ]
      },
      {
        "name": "嘉兴",
        "county": [
          {
            "name": "嘉兴",
            "code": "CN101210301",
            "name_en": "jiaxing"
          },
          {
            "name": "嘉善",
            "code": "CN101210302",
            "name_en": "jiashan"
          },
          {
            "name": "海宁",
            "code": "CN101210303",
            "name_en": "haining"
          },
          {
            "name": "桐乡",
            "code": "CN101210304",
            "name_en": "tongxiang"
          },
          {
            "name": "平湖",
            "code": "CN101210305",
            "name_en": "pinghu"
          },
          {
            "name": "海盐",
            "code": "CN101210306",
            "name_en": "haiyan"
          }
        ]
      },
      {
        "name": "宁波",
        "county": [
          {
            "name": "宁波",
            "code": "CN101210401",
            "name_en": "ningbo"
          },
          {
            "name": "慈溪",
            "code": "CN101210403",
            "name_en": "cixi"
          },
          {
            "name": "余姚",
            "code": "CN101210404",
            "name_en": "yuyao"
          },
          {
            "name": "奉化",
            "code": "CN101210405",
            "name_en": "fenghua"
          },
          {
            "name": "象山",
            "code": "CN101210406",
            "name_en": "xiangshan"
          },
          {
            "name": "宁海",
            "code": "CN101210408",
            "name_en": "ninghai"
          },
          {
            "name": "北仑",
            "code": "CN101210410",
            "name_en": "beilun"
          },
          {
            "name": "鄞州",
            "code": "CN101210411",
            "name_en": "yinzhou"
          },
          {
            "name": "镇海",
            "code": "CN101210412",
            "name_en": "zhenhai"
          }
        ]
      },
      {
        "name": "绍兴",
        "county": [
          {
            "name": "绍兴",
            "code": "CN101210501",
            "name_en": "shaoxing"
          },
          {
            "name": "诸暨",
            "code": "CN101210502",
            "name_en": "zhuji"
          },
          {
            "name": "上虞",
            "code": "CN101210503",
            "name_en": "shangyu"
          },
          {
            "name": "新昌",
            "code": "CN101210504",
            "name_en": "xinchang"
          },
          {
            "name": "嵊州",
            "code": "CN101210505",
            "name_en": "shengzhou"
          }
        ]
      },
      {
        "name": "台州",
        "county": [
          {
            "name": "台州",
            "code": "CN101210601",
            "name_en": "taizhou"
          },
          {
            "name": "玉环",
            "code": "CN101210603",
            "name_en": "yuhuan"
          },
          {
            "name": "三门",
            "code": "CN101210604",
            "name_en": "sanmen"
          },
          {
            "name": "天台",
            "code": "CN101210605",
            "name_en": "tiantai"
          },
          {
            "name": "仙居",
            "code": "CN101210606",
            "name_en": "xianju"
          },
          {
            "name": "温岭",
            "code": "CN101210607",
            "name_en": "wenling"
          },
          {
            "name": "洪家",
            "code": "CN101210609",
            "name_en": "hongjia"
          },
          {
            "name": "临海",
            "code": "CN101210610",
            "name_en": "linhai"
          },
          {
            "name": "椒江",
            "code": "CN101210611",
            "name_en": "jiaojiang"
          },
          {
            "name": "黄岩",
            "code": "CN101210612",
            "name_en": "huangyan"
          },
          {
            "name": "路桥",
            "code": "CN101210613",
            "name_en": "luqiao"
          }
        ]
      },
      {
        "name": "温州",
        "county": [
          {
            "name": "温州",
            "code": "CN101210701",
            "name_en": "wenzhou"
          },
          {
            "name": "泰顺",
            "code": "CN101210702",
            "name_en": "taishun"
          },
          {
            "name": "文成",
            "code": "CN101210703",
            "name_en": "wencheng"
          },
          {
            "name": "平阳",
            "code": "CN101210704",
            "name_en": "pingyang"
          },
          {
            "name": "瑞安",
            "code": "CN101210705",
            "name_en": "ruian"
          },
          {
            "name": "洞头",
            "code": "CN101210706",
            "name_en": "dongtou"
          },
          {
            "name": "乐清",
            "code": "CN101210707",
            "name_en": "yueqing"
          },
          {
            "name": "永嘉",
            "code": "CN101210708",
            "name_en": "yongjia"
          },
          {
            "name": "苍南",
            "code": "CN101210709",
            "name_en": "cangnan"
          }
        ]
      },
      {
        "name": "丽水",
        "county": [
          {
            "name": "丽水",
            "code": "CN101210801",
            "name_en": "lishui"
          },
          {
            "name": "遂昌",
            "code": "CN101210802",
            "name_en": "suichang"
          },
          {
            "name": "龙泉",
            "code": "CN101210803",
            "name_en": "longquan"
          },
          {
            "name": "缙云",
            "code": "CN101210804",
            "name_en": "jinyun"
          },
          {
            "name": "青田",
            "code": "CN101210805",
            "name_en": "qingtian"
          },
          {
            "name": "云和",
            "code": "CN101210806",
            "name_en": "yunhe"
          },
          {
            "name": "庆元",
            "code": "CN101210807",
            "name_en": "qingyuan"
          },
          {
            "name": "松阳",
            "code": "CN101210808",
            "name_en": "songyang"
          },
          {
            "name": "景宁",
            "code": "CN101210809",
            "name_en": "jingning"
          }
        ]
      },
      {
        "name": "金华",
        "county": [
          {
            "name": "金华",
            "code": "CN101210901",
            "name_en": "jinhua"
          },
          {
            "name": "浦江",
            "code": "CN101210902",
            "name_en": "pujiang"
          },
          {
            "name": "兰溪",
            "code": "CN101210903",
            "name_en": "lanxi"
          },
          {
            "name": "义乌",
            "code": "CN101210904",
            "name_en": "yiwu"
          },
          {
            "name": "东阳",
            "code": "CN101210905",
            "name_en": "dongyang"
          },
          {
            "name": "武义",
            "code": "CN101210906",
            "name_en": "wuyi"
          },
          {
            "name": "永康",
            "code": "CN101210907",
            "name_en": "yongkang"
          },
          {
            "name": "磐安",
            "code": "CN101210908",
            "name_en": "panan"
          }
        ]
      },
      {
        "name": "衢州",
        "county": [
          {
            "name": "衢州",
            "code": "CN101211001",
            "name_en": "quzhou"
          },
          {
            "name": "常山",
            "code": "CN101211002",
            "name_en": "changshan"
          },
          {
            "name": "开化",
            "code": "CN101211003",
            "name_en": "kaihua"
          },
          {
            "name": "龙游",
            "code": "CN101211004",
            "name_en": "longyou"
          },
          {
            "name": "江山",
            "code": "CN101211005",
            "name_en": "jiangshan"
          },
          {
            "name": "衢江",
            "code": "CN101211006",
            "name_en": "qujiang"
          }
        ]
      },
      {
        "name": "舟山",
        "county": [
          {
            "name": "舟山",
            "code": "CN101211101",
            "name_en": "zhoushan"
          },
          {
            "name": "嵊泗",
            "code": "CN101211102",
            "name_en": "shengsi"
          },
          {
            "name": "岱山",
            "code": "CN101211104",
            "name_en": "daishan"
          },
          {
            "name": "普陀",
            "code": "CN101211105",
            "name_en": "putuo"
          },
          {
            "name": "定海",
            "code": "CN101211106",
            "name_en": "dinghai"
          }
        ]
      }
    ]
  },
  {
    "name": "安徽",
    "name_en": "anhui",
    "city": [
      {
        "name": "合肥",
        "county": [
          {
            "name": "合肥",
            "code": "CN101220101",
            "name_en": "hefei"
          },
          {
            "name": "长丰",
            "code": "CN101220102",
            "name_en": "changfeng"
          },
          {
            "name": "肥东",
            "code": "CN101220103",
            "name_en": "feidong"
          },
          {
            "name": "肥西",
            "code": "CN101220104",
            "name_en": "feixi"
          },
          {
            "name": "巢湖",
            "code": "CN101220105",
            "name_en": "chaohu"
          },
          {
            "name": "庐江",
            "code": "CN101220106",
            "name_en": "lujiang"
          }
        ]
      },
      {
        "name": "蚌埠",
        "county": [
          {
            "name": "蚌埠",
            "code": "CN101220201",
            "name_en": "bengbu"
          },
          {
            "name": "怀远",
            "code": "CN101220202",
            "name_en": "huaiyuan"
          },
          {
            "name": "固镇",
            "code": "CN101220203",
            "name_en": "guzhen"
          },
          {
            "name": "五河",
            "code": "CN101220204",
            "name_en": "wuhe"
          }
        ]
      },
      {
        "name": "芜湖",
        "county": [
          {
            "name": "芜湖",
            "code": "CN101220301",
            "name_en": "wuhu"
          },
          {
            "name": "繁昌",
            "code": "CN101220302",
            "name_en": "fanyang"
          },
          {
            "name": "芜湖县",
            "code": "CN101220303",
            "name_en": "wuhuxian"
          },
          {
            "name": "南陵",
            "code": "CN101220304",
            "name_en": "nanling"
          },
          {
            "name": "无为",
            "code": "CN101220305",
            "name_en": "wuwei"
          }
        ]
      },
      {
        "name": "淮南",
        "county": [
          {
            "name": "淮南",
            "code": "CN101220401",
            "name_en": "huainan"
          },
          {
            "name": "凤台",
            "code": "CN101220402",
            "name_en": "fengtai"
          },
          {
            "name": "潘集",
            "code": "CN101220403",
            "name_en": "panji"
          }
        ]
      },
      {
        "name": "马鞍山",
        "county": [
          {
            "name": "马鞍山",
            "code": "CN101220501",
            "name_en": "maanshan"
          },
          {
            "name": "当涂",
            "code": "CN101220502",
            "name_en": "dangtu"
          },
          {
            "name": "含山",
            "code": "CN101220503",
            "name_en": "hanshan"
          },
          {
            "name": "和县",
            "code": "CN101220504",
            "name_en": "hexian"
          }
        ]
      },
      {
        "name": "安庆",
        "county": [
          {
            "name": "安庆",
            "code": "CN101220601",
            "name_en": "anqing"
          },
          {
            "name": "枞阳",
            "code": "CN101220602",
            "name_en": "zongyang"
          },
          {
            "name": "太湖",
            "code": "CN101220603",
            "name_en": "taihu"
          },
          {
            "name": "潜山",
            "code": "CN101220604",
            "name_en": "qianshan"
          },
          {
            "name": "怀宁",
            "code": "CN101220605",
            "name_en": "huaining"
          },
          {
            "name": "宿松",
            "code": "CN101220606",
            "name_en": "susong"
          },
          {
            "name": "望江",
            "code": "CN101220607",
            "name_en": "wangjiang"
          },
          {
            "name": "岳西",
            "code": "CN101220608",
            "name_en": "yuexi"
          },
          {
            "name": "桐城",
            "code": "CN101220609",
            "name_en": "tongcheng"
          }
        ]
      },
      {
        "name": "宿州",
        "county": [
          {
            "name": "宿州",
            "code": "CN101220701",
            "name_en": "suzhou"
          },
          {
            "name": "砀山",
            "code": "CN101220702",
            "name_en": "dangshan"
          },
          {
            "name": "灵璧",
            "code": "CN101220703",
            "name_en": "lingbi"
          },
          {
            "name": "泗县",
            "code": "CN101220704",
            "name_en": "sixian"
          },
          {
            "name": "萧县",
            "code": "CN101220705",
            "name_en": "xiaoxian"
          }
        ]
      },
      {
        "name": "阜阳",
        "county": [
          {
            "name": "阜阳",
            "code": "CN101220801",
            "name_en": "fuyang"
          },
          {
            "name": "阜南",
            "code": "CN101220802",
            "name_en": "funan"
          },
          {
            "name": "颍上",
            "code": "CN101220803",
            "name_en": "yingshang"
          },
          {
            "name": "临泉",
            "code": "CN101220804",
            "name_en": "linquan"
          },
          {
            "name": "界首",
            "code": "CN101220805",
            "name_en": "jieshou"
          },
          {
            "name": "太和",
            "code": "CN101220806",
            "name_en": "taihe"
          }
        ]
      },
      {
        "name": "亳州",
        "county": [
          {
            "name": "亳州",
            "code": "CN101220901",
            "name_en": "bozhou"
          },
          {
            "name": "涡阳",
            "code": "CN101220902",
            "name_en": "guoyang"
          },
          {
            "name": "利辛",
            "code": "CN101220903",
            "name_en": "lixin"
          },
          {
            "name": "蒙城",
            "code": "CN101220904",
            "name_en": "mengcheng"
          }
        ]
      },
      {
        "name": "黄山",
        "county": [
          {
            "name": "黄山",
            "code": "CN101221001",
            "name_en": "huangshan"
          },
          {
            "name": "黄山区",
            "code": "CN101221002",
            "name_en": "huangshanqu"
          },
          {
            "name": "屯溪",
            "code": "CN101221003",
            "name_en": "tunxi"
          },
          {
            "name": "祁门",
            "code": "CN101221004",
            "name_en": "qimen"
          },
          {
            "name": "黟县",
            "code": "CN101221005",
            "name_en": "yixian"
          },
          {
            "name": "歙县",
            "code": "CN101221006",
            "name_en": "shexian"
          },
          {
            "name": "休宁",
            "code": "CN101221007",
            "name_en": "xiuning"
          },
          {
            "name": "黄山风景区",
            "code": "CN101221008",
            "name_en": "huangshanfengjingqu"
          }
        ]
      },
      {
        "name": "滁州",
        "county": [
          {
            "name": "滁州",
            "code": "CN101221101",
            "name_en": "chuzhou"
          },
          {
            "name": "凤阳",
            "code": "CN101221102",
            "name_en": "fengyang"
          },
          {
            "name": "明光",
            "code": "CN101221103",
            "name_en": "mingguang"
          },
          {
            "name": "定远",
            "code": "CN101221104",
            "name_en": "dingyuan"
          },
          {
            "name": "全椒",
            "code": "CN101221105",
            "name_en": "quanjiao"
          },
          {
            "name": "来安",
            "code": "CN101221106",
            "name_en": "laian"
          },
          {
            "name": "天长",
            "code": "CN101221107",
            "name_en": "tianchang"
          }
        ]
      },
      {
        "name": "淮北",
        "county": [
          {
            "name": "淮北",
            "code": "CN101221201",
            "name_en": "huaibei"
          },
          {
            "name": "濉溪",
            "code": "CN101221202",
            "name_en": "suixi"
          }
        ]
      },
      {
        "name": "铜陵",
        "county": [
          {
            "name": "铜陵",
            "code": "CN101221301",
            "name_en": "tongling"
          }
        ]
      },
      {
        "name": "宣城",
        "county": [
          {
            "name": "宣城",
            "code": "CN101221401",
            "name_en": "xuancheng"
          },
          {
            "name": "泾县",
            "code": "CN101221402",
            "name_en": "jingxian"
          },
          {
            "name": "旌德",
            "code": "CN101221403",
            "name_en": "jingde"
          },
          {
            "name": "宁国",
            "code": "CN101221404",
            "name_en": "ningguo"
          },
          {
            "name": "绩溪",
            "code": "CN101221405",
            "name_en": "jixi"
          },
          {
            "name": "广德",
            "code": "CN101221406",
            "name_en": "guangde"
          },
          {
            "name": "郎溪",
            "code": "CN101221407",
            "name_en": "langxi"
          }
        ]
      },
      {
        "name": "六安",
        "county": [
          {
            "name": "六安",
            "code": "CN101221501",
            "name_en": "luan"
          },
          {
            "name": "霍邱",
            "code": "CN101221502",
            "name_en": "huoqiu"
          },
          {
            "name": "寿县",
            "code": "CN101221503",
            "name_en": "shouxian"
          },
          {
            "name": "金寨",
            "code": "CN101221505",
            "name_en": "jinzhai"
          },
          {
            "name": "霍山",
            "code": "CN101221506",
            "name_en": "huoshan"
          },
          {
            "name": "舒城",
            "code": "CN101221507",
            "name_en": "shucheng"
          }
        ]
      },
      {
        "name": "池州",
        "county": [
          {
            "name": "池州",
            "code": "CN101221701",
            "name_en": "chizhou"
          },
          {
            "name": "东至",
            "code": "CN101221702",
            "name_en": "dongzhi"
          },
          {
            "name": "青阳",
            "code": "CN101221703",
            "name_en": "qingyang"
          },
          {
            "name": "九华山",
            "code": "CN101221704",
            "name_en": "jiuhuashan"
          },
          {
            "name": "石台",
            "code": "CN101221705",
            "name_en": "shitai"
          }
        ]
      }
    ]
  },
  {
    "name": "福建",
    "name_en": "fujian",
    "city": [
      {
        "name": "福州",
        "county": [
          {
            "name": "福州",
            "code": "CN101230101",
            "name_en": "fuzhou"
          },
          {
            "name": "闽清",
            "code": "CN101230102",
            "name_en": "minqing"
          },
          {
            "name": "闽侯",
            "code": "CN101230103",
            "name_en": "minhou"
          },
          {
            "name": "罗源",
            "code": "CN101230104",
            "name_en": "luoyuan"
          },
          {
            "name": "连江",
            "code": "CN101230105",
            "name_en": "lianjiang"
          },
          {
            "name": "永泰",
            "code": "CN101230107",
            "name_en": "yongtai"
          },
          {
            "name": "平潭",
            "code": "CN101230108",
            "name_en": "pingtan"
          },
          {
            "name": "长乐",
            "code": "CN101230110",
            "name_en": "changle"
          },
          {
            "name": "福清",
            "code": "CN101230111",
            "name_en": "fuqing"
          }
        ]
      },
      {
        "name": "厦门",
        "county": [
          {
            "name": "厦门",
            "code": "CN101230201",
            "name_en": "xiamen"
          },
          {
            "name": "同安",
            "code": "CN101230202",
            "name_en": "tongan"
          }
        ]
      },
      {
        "name": "宁德",
        "county": [
          {
            "name": "宁德",
            "code": "CN101230301",
            "name_en": "ningde"
          },
          {
            "name": "古田",
            "code": "CN101230302",
            "name_en": "gutian"
          },
          {
            "name": "霞浦",
            "code": "CN101230303",
            "name_en": "xiapu"
          },
          {
            "name": "寿宁",
            "code": "CN101230304",
            "name_en": "shouning"
          },
          {
            "name": "周宁",
            "code": "CN101230305",
            "name_en": "zhouning"
          },
          {
            "name": "福安",
            "code": "CN101230306",
            "name_en": "fuan"
          },
          {
            "name": "柘荣",
            "code": "CN101230307",
            "name_en": "zherong"
          },
          {
            "name": "福鼎",
            "code": "CN101230308",
            "name_en": "fuding"
          },
          {
            "name": "屏南",
            "code": "CN101230309",
            "name_en": "pingnan"
          }
        ]
      },
      {
        "name": "莆田",
        "county": [
          {
            "name": "莆田",
            "code": "CN101230401",
            "name_en": "putian"
          },
          {
            "name": "仙游",
            "code": "CN101230402",
            "name_en": "xianyou"
          },
          {
            "name": "秀屿港",
            "code": "CN101230403",
            "name_en": "xiuyugang"
          },
          {
            "name": "涵江",
            "code": "CN101230404",
            "name_en": "hanjiang"
          },
          {
            "name": "秀屿",
            "code": "CN101230405",
            "name_en": "xiuyu"
          },
          {
            "name": "荔城",
            "code": "CN101230406",
            "name_en": "licheng"
          },
          {
            "name": "城厢",
            "code": "CN101230407",
            "name_en": "chengxiang"
          }
        ]
      },
      {
        "name": "泉州",
        "county": [
          {
            "name": "泉州",
            "code": "CN101230501",
            "name_en": "quanzhou"
          },
          {
            "name": "安溪",
            "code": "CN101230502",
            "name_en": "anxi"
          },
          {
            "name": "永春",
            "code": "CN101230504",
            "name_en": "yongchun"
          },
          {
            "name": "德化",
            "code": "CN101230505",
            "name_en": "dehua"
          },
          {
            "name": "南安",
            "code": "CN101230506",
            "name_en": "nanan"
          },
          {
            "name": "崇武",
            "code": "CN101230507",
            "name_en": "chongwu"
          },
          {
            "name": "惠安",
            "code": "CN101230508",
            "name_en": "huian"
          },
          {
            "name": "晋江",
            "code": "CN101230509",
            "name_en": "jinjiang"
          },
          {
            "name": "石狮",
            "code": "CN101230510",
            "name_en": "shishi"
          }
        ]
      },
      {
        "name": "漳州",
        "county": [
          {
            "name": "漳州",
            "code": "CN101230601",
            "name_en": "zhangzhou"
          },
          {
            "name": "长泰",
            "code": "CN101230602",
            "name_en": "changtai"
          },
          {
            "name": "南靖",
            "code": "CN101230603",
            "name_en": "nanjing"
          },
          {
            "name": "平和",
            "code": "CN101230604",
            "name_en": "pinghe"
          },
          {
            "name": "龙海",
            "code": "CN101230605",
            "name_en": "longhai"
          },
          {
            "name": "漳浦",
            "code": "CN101230606",
            "name_en": "zhangpu"
          },
          {
            "name": "诏安",
            "code": "CN101230607",
            "name_en": "zhaoan"
          },
          {
            "name": "东山",
            "code": "CN101230608",
            "name_en": "dongshan"
          },
          {
            "name": "云霄",
            "code": "CN101230609",
            "name_en": "yunxiao"
          },
          {
            "name": "华安",
            "code": "CN101230610",
            "name_en": "huaan"
          }
        ]
      },
      {
        "name": "龙岩",
        "county": [
          {
            "name": "龙岩",
            "code": "CN101230701",
            "name_en": "longyan"
          },
          {
            "name": "长汀",
            "code": "CN101230702",
            "name_en": "changting"
          },
          {
            "name": "连城",
            "code": "CN101230703",
            "name_en": "liancheng"
          },
          {
            "name": "武平",
            "code": "CN101230704",
            "name_en": "wuping"
          },
          {
            "name": "上杭",
            "code": "CN101230705",
            "name_en": "shanghang"
          },
          {
            "name": "永定",
            "code": "CN101230706",
            "name_en": "yongding"
          },
          {
            "name": "漳平",
            "code": "CN101230707",
            "name_en": "zhangping"
          }
        ]
      },
      {
        "name": "三明",
        "county": [
          {
            "name": "三明",
            "code": "CN101230801",
            "name_en": "sanming"
          },
          {
            "name": "宁化",
            "code": "CN101230802",
            "name_en": "ninghua"
          },
          {
            "name": "清流",
            "code": "CN101230803",
            "name_en": "qingliu"
          },
          {
            "name": "泰宁",
            "code": "CN101230804",
            "name_en": "taining"
          },
          {
            "name": "将乐",
            "code": "CN101230805",
            "name_en": "jiangle"
          },
          {
            "name": "建宁",
            "code": "CN101230806",
            "name_en": "jianning"
          },
          {
            "name": "明溪",
            "code": "CN101230807",
            "name_en": "mingxi"
          },
          {
            "name": "沙县",
            "code": "CN101230808",
            "name_en": "shaxian"
          },
          {
            "name": "尤溪",
            "code": "CN101230809",
            "name_en": "youxi"
          },
          {
            "name": "永安",
            "code": "CN101230810",
            "name_en": "yongan"
          },
          {
            "name": "大田",
            "code": "CN101230811",
            "name_en": "datian"
          }
        ]
      },
      {
        "name": "南平",
        "county": [
          {
            "name": "南平",
            "code": "CN101230901",
            "name_en": "nanping"
          },
          {
            "name": "顺昌",
            "code": "CN101230902",
            "name_en": "shunchang"
          },
          {
            "name": "光泽",
            "code": "CN101230903",
            "name_en": "guangze"
          },
          {
            "name": "邵武",
            "code": "CN101230904",
            "name_en": "shaowu"
          },
          {
            "name": "武夷山",
            "code": "CN101230905",
            "name_en": "wuyishan"
          },
          {
            "name": "浦城",
            "code": "CN101230906",
            "name_en": "pucheng"
          },
          {
            "name": "建阳",
            "code": "CN101230907",
            "name_en": "jianyang"
          },
          {
            "name": "松溪",
            "code": "CN101230908",
            "name_en": "songxi"
          },
          {
            "name": "政和",
            "code": "CN101230909",
            "name_en": "zhenghe"
          },
          {
            "name": "建瓯",
            "code": "CN101230910",
            "name_en": "jianou"
          }
        ]
      },
      {
        "name": "钓鱼岛",
        "county": [
          {
            "name": "钓鱼岛",
            "code": "CN101231001",
            "name_en": "diaoyudao"
          }
        ]
      }
    ]
  },
  {
    "name": "江西",
    "name_en": "jiangxi",
    "city": [
      {
        "name": "南昌",
        "county": [
          {
            "name": "南昌",
            "code": "CN101240101",
            "name_en": "nanchang"
          },
          {
            "name": "新建",
            "code": "CN101240102",
            "name_en": "xinjian"
          },
          {
            "name": "南昌县",
            "code": "CN101240103",
            "name_en": "nanchangxian"
          },
          {
            "name": "安义",
            "code": "CN101240104",
            "name_en": "anyi"
          },
          {
            "name": "进贤",
            "code": "CN101240105",
            "name_en": "jinxian"
          }
        ]
      },
      {
        "name": "九江",
        "county": [
          {
            "name": "九江",
            "code": "CN101240201",
            "name_en": "jiujiang"
          },
          {
            "name": "瑞昌",
            "code": "CN101240202",
            "name_en": "ruichang"
          },
          {
            "name": "庐山",
            "code": "CN101240203",
            "name_en": "lushan"
          },
          {
            "name": "武宁",
            "code": "CN101240204",
            "name_en": "wuning"
          },
          {
            "name": "德安",
            "code": "CN101240205",
            "name_en": "dean"
          },
          {
            "name": "永修",
            "code": "CN101240206",
            "name_en": "yongxiu"
          },
          {
            "name": "湖口",
            "code": "CN101240207",
            "name_en": "hukou"
          },
          {
            "name": "彭泽",
            "code": "CN101240208",
            "name_en": "pengze"
          },
          {
            "name": "星子",
            "code": "CN101240209",
            "name_en": "xingzi"
          },
          {
            "name": "都昌",
            "code": "CN101240210",
            "name_en": "duchang"
          },
          {
            "name": "修水",
            "code": "CN101240212",
            "name_en": "xiushui"
          }
        ]
      },
      {
        "name": "上饶",
        "county": [
          {
            "name": "上饶",
            "code": "CN101240301",
            "name_en": "shangrao"
          },
          {
            "name": "鄱阳",
            "code": "CN101240302",
            "name_en": "poyang"
          },
          {
            "name": "婺源",
            "code": "CN101240303",
            "name_en": "wuyuan"
          },
          {
            "name": "余干",
            "code": "CN101240305",
            "name_en": "yugan"
          },
          {
            "name": "万年",
            "code": "CN101240306",
            "name_en": "wannian"
          },
          {
            "name": "德兴",
            "code": "CN101240307",
            "name_en": "dexing"
          },
          {
            "name": "上饶县",
            "code": "CN101240308",
            "name_en": "shangraoxian"
          },
          {
            "name": "弋阳",
            "code": "CN101240309",
            "name_en": "yiyang"
          },
          {
            "name": "横峰",
            "code": "CN101240310",
            "name_en": "hengfeng"
          },
          {
            "name": "铅山",
            "code": "CN101240311",
            "name_en": "yanshan"
          },
          {
            "name": "玉山",
            "code": "CN101240312",
            "name_en": "yushan"
          },
          {
            "name": "广丰",
            "code": "CN101240313",
            "name_en": "guangfeng"
          }
        ]
      },
      {
        "name": "抚州",
        "county": [
          {
            "name": "抚州",
            "code": "CN101240401",
            "name_en": "fuzhou"
          },
          {
            "name": "广昌",
            "code": "CN101240402",
            "name_en": "guangchang"
          },
          {
            "name": "乐安",
            "code": "CN101240403",
            "name_en": "anle"
          },
          {
            "name": "崇仁",
            "code": "CN101240404",
            "name_en": "chongren"
          },
          {
            "name": "金溪",
            "code": "CN101240405",
            "name_en": "jinxi"
          },
          {
            "name": "资溪",
            "code": "CN101240406",
            "name_en": "zixi"
          },
          {
            "name": "宜黄",
            "code": "CN101240407",
            "name_en": "yihuang"
          },
          {
            "name": "南城",
            "code": "CN101240408",
            "name_en": "nancheng"
          },
          {
            "name": "南丰",
            "code": "CN101240409",
            "name_en": "nanfeng"
          },
          {
            "name": "黎川",
            "code": "CN101240410",
            "name_en": "lichuan"
          },
          {
            "name": "东乡",
            "code": "CN101240411",
            "name_en": "dongxiang"
          }
        ]
      },
      {
        "name": "宜春",
        "county": [
          {
            "name": "宜春",
            "code": "CN101240501",
            "name_en": "yichun"
          },
          {
            "name": "铜鼓",
            "code": "CN101240502",
            "name_en": "tonggu"
          },
          {
            "name": "宜丰",
            "code": "CN101240503",
            "name_en": "yifeng"
          },
          {
            "name": "万载",
            "code": "CN101240504",
            "name_en": "wanzai"
          },
          {
            "name": "上高",
            "code": "CN101240505",
            "name_en": "shanggao"
          },
          {
            "name": "靖安",
            "code": "CN101240506",
            "name_en": "jingan"
          },
          {
            "name": "奉新",
            "code": "CN101240507",
            "name_en": "fengxin"
          },
          {
            "name": "高安",
            "code": "CN101240508",
            "name_en": "gaoan"
          },
          {
            "name": "樟树",
            "code": "CN101240509",
            "name_en": "zhangshu"
          },
          {
            "name": "丰城",
            "code": "CN101240510",
            "name_en": "fengcheng"
          }
        ]
      },
      {
        "name": "吉安",
        "county": [
          {
            "name": "吉安",
            "code": "CN101240601",
            "name_en": "jian"
          },
          {
            "name": "吉安县",
            "code": "CN101240602",
            "name_en": "jianxian"
          },
          {
            "name": "吉水",
            "code": "CN101240603",
            "name_en": "jishui"
          },
          {
            "name": "新干",
            "code": "CN101240604",
            "name_en": "xingan"
          },
          {
            "name": "峡江",
            "code": "CN101240605",
            "name_en": "xiajiang"
          },
          {
            "name": "永丰",
            "code": "CN101240606",
            "name_en": "yongfeng"
          },
          {
            "name": "永新",
            "code": "CN101240607",
            "name_en": "yongxin"
          },
          {
            "name": "井冈山",
            "code": "CN101240608",
            "name_en": "jinggangshan"
          },
          {
            "name": "万安",
            "code": "CN101240609",
            "name_en": "wanan"
          },
          {
            "name": "遂川",
            "code": "CN101240610",
            "name_en": "suichuan"
          },
          {
            "name": "泰和",
            "code": "CN101240611",
            "name_en": "taihe"
          },
          {
            "name": "安福",
            "code": "CN101240612",
            "name_en": "anfu"
          },
          {
            "name": "宁冈",
            "code": "CN101240613",
            "name_en": "ninggang"
          }
        ]
      },
      {
        "name": "赣州",
        "county": [
          {
            "name": "赣州",
            "code": "CN101240701",
            "name_en": "ganzhou"
          },
          {
            "name": "崇义",
            "code": "CN101240702",
            "name_en": "chongyi"
          },
          {
            "name": "上犹",
            "code": "CN101240703",
            "name_en": "shangyou"
          },
          {
            "name": "南康",
            "code": "CN101240704",
            "name_en": "nankang"
          },
          {
            "name": "大余",
            "code": "CN101240705",
            "name_en": "dayu"
          },
          {
            "name": "信丰",
            "code": "CN101240706",
            "name_en": "xinfeng"
          },
          {
            "name": "宁都",
            "code": "CN101240707",
            "name_en": "ningdu"
          },
          {
            "name": "石城",
            "code": "CN101240708",
            "name_en": "shicheng"
          },
          {
            "name": "瑞金",
            "code": "CN101240709",
            "name_en": "ruijin"
          },
          {
            "name": "于都",
            "code": "CN101240710",
            "name_en": "yudu"
          },
          {
            "name": "会昌",
            "code": "CN101240711",
            "name_en": "huichang"
          },
          {
            "name": "安远",
            "code": "CN101240712",
            "name_en": "anyuan"
          },
          {
            "name": "全南",
            "code": "CN101240713",
            "name_en": "quannan"
          },
          {
            "name": "龙南",
            "code": "CN101240714",
            "name_en": "longnan"
          },
          {
            "name": "定南",
            "code": "CN101240715",
            "name_en": "dingnan"
          },
          {
            "name": "寻乌",
            "code": "CN101240716",
            "name_en": "xunwu"
          },
          {
            "name": "兴国",
            "code": "CN101240717",
            "name_en": "xingguo"
          },
          {
            "name": "赣县",
            "code": "CN101240718",
            "name_en": "ganxian"
          }
        ]
      },
      {
        "name": "景德镇",
        "county": [
          {
            "name": "景德镇",
            "code": "CN101240801",
            "name_en": "jingdezhen"
          },
          {
            "name": "乐平",
            "code": "CN101240802",
            "name_en": "leping"
          },
          {
            "name": "浮梁",
            "code": "CN101240803",
            "name_en": "fuliang"
          }
        ]
      },
      {
        "name": "萍乡",
        "county": [
          {
            "name": "萍乡",
            "code": "CN101240901",
            "name_en": "pingxiang"
          },
          {
            "name": "莲花",
            "code": "CN101240902",
            "name_en": "lianhua"
          },
          {
            "name": "上栗",
            "code": "CN101240903",
            "name_en": "shangli"
          },
          {
            "name": "安源",
            "code": "CN101240904",
            "name_en": "anyuan"
          },
          {
            "name": "芦溪",
            "code": "CN101240905",
            "name_en": "luxi"
          },
          {
            "name": "湘东",
            "code": "CN101240906",
            "name_en": "xiangdong"
          }
        ]
      },
      {
        "name": "新余",
        "county": [
          {
            "name": "新余",
            "code": "CN101241001",
            "name_en": "xinyu"
          },
          {
            "name": "分宜",
            "code": "CN101241002",
            "name_en": "fenyi"
          }
        ]
      },
      {
        "name": "鹰潭",
        "county": [
          {
            "name": "鹰潭",
            "code": "CN101241101",
            "name_en": "yingtan"
          },
          {
            "name": "余江",
            "code": "CN101241102",
            "name_en": "yujiang"
          },
          {
            "name": "贵溪",
            "code": "CN101241103",
            "name_en": "guixi"
          }
        ]
      }
    ]
  },
  {
    "name": "湖南",
    "name_en": "hunan",
    "city": [
      {
        "name": "长沙",
        "county": [
          {
            "name": "长沙",
            "code": "CN101250101",
            "name_en": "changsha"
          },
          {
            "name": "宁乡",
            "code": "CN101250102",
            "name_en": "ningxiang"
          },
          {
            "name": "浏阳",
            "code": "CN101250103",
            "name_en": "liuyang"
          },
          {
            "name": "马坡岭",
            "code": "CN101250104",
            "name_en": "mapoling"
          },
          {
            "name": "望城",
            "code": "CN101250105",
            "name_en": "wangcheng"
          }
        ]
      },
      {
        "name": "湘潭",
        "county": [
          {
            "name": "湘潭",
            "code": "CN101250201",
            "name_en": "xiangtan"
          },
          {
            "name": "韶山",
            "code": "CN101250202",
            "name_en": "shaoshan"
          },
          {
            "name": "湘乡",
            "code": "CN101250203",
            "name_en": "xiangxiang"
          }
        ]
      },
      {
        "name": "株洲",
        "county": [
          {
            "name": "株洲",
            "code": "CN101250301",
            "name_en": "zhuzhou"
          },
          {
            "name": "攸县",
            "code": "CN101250302",
            "name_en": "youxian"
          },
          {
            "name": "醴陵",
            "code": "CN101250303",
            "name_en": "liling"
          },
          {
            "name": "茶陵",
            "code": "CN101250305",
            "name_en": "chaling"
          },
          {
            "name": "炎陵",
            "code": "CN101250306",
            "name_en": "yanling"
          }
        ]
      },
      {
        "name": "衡阳",
        "county": [
          {
            "name": "衡阳",
            "code": "CN101250401",
            "name_en": "hengyang"
          },
          {
            "name": "衡山",
            "code": "CN101250402",
            "name_en": "hengshan"
          },
          {
            "name": "衡东",
            "code": "CN101250403",
            "name_en": "hengdong"
          },
          {
            "name": "祁东",
            "code": "CN101250404",
            "name_en": "qidong"
          },
          {
            "name": "衡阳县",
            "code": "CN101250405",
            "name_en": "hengyangxian"
          },
          {
            "name": "常宁",
            "code": "CN101250406",
            "name_en": "changning"
          },
          {
            "name": "衡南",
            "code": "CN101250407",
            "name_en": "hengnan"
          },
          {
            "name": "耒阳",
            "code": "CN101250408",
            "name_en": "leiyang"
          },
          {
            "name": "南岳",
            "code": "CN101250409",
            "name_en": "nanyue"
          }
        ]
      },
      {
        "name": "郴州",
        "county": [
          {
            "name": "郴州",
            "code": "CN101250501",
            "name_en": "chenzhou"
          },
          {
            "name": "桂阳",
            "code": "CN101250502",
            "name_en": "guiyang"
          },
          {
            "name": "嘉禾",
            "code": "CN101250503",
            "name_en": "jiahe"
          },
          {
            "name": "宜章",
            "code": "CN101250504",
            "name_en": "yizhang"
          },
          {
            "name": "临武",
            "code": "CN101250505",
            "name_en": "linwu"
          },
          {
            "name": "资兴",
            "code": "CN101250507",
            "name_en": "zixing"
          },
          {
            "name": "汝城",
            "code": "CN101250508",
            "name_en": "rucheng"
          },
          {
            "name": "安仁",
            "code": "CN101250509",
            "name_en": "anren"
          },
          {
            "name": "永兴",
            "code": "CN101250510",
            "name_en": "yongxing"
          },
          {
            "name": "桂东",
            "code": "CN101250511",
            "name_en": "guidong"
          },
          {
            "name": "苏仙",
            "code": "CN101250512",
            "name_en": "suxian"
          }
        ]
      },
      {
        "name": "常德",
        "county": [
          {
            "name": "常德",
            "code": "CN101250601",
            "name_en": "changde"
          },
          {
            "name": "安乡",
            "code": "CN101250602",
            "name_en": "anxiang"
          },
          {
            "name": "桃源",
            "code": "CN101250603",
            "name_en": "taoyuan"
          },
          {
            "name": "汉寿",
            "code": "CN101250604",
            "name_en": "hanshou"
          },
          {
            "name": "澧县",
            "code": "CN101250605",
            "name_en": "lixian"
          },
          {
            "name": "临澧",
            "code": "CN101250606",
            "name_en": "linli"
          },
          {
            "name": "石门",
            "code": "CN101250607",
            "name_en": "shimen"
          },
          {
            "name": "津市",
            "code": "CN101250608",
            "name_en": "jinshi"
          }
        ]
      },
      {
        "name": "益阳",
        "county": [
          {
            "name": "益阳",
            "code": "CN101250700",
            "name_en": "yiyang"
          },
          {
            "name": "赫山区",
            "code": "CN101250701",
            "name_en": "heshanqu"
          },
          {
            "name": "南县",
            "code": "CN101250702",
            "name_en": "nanxian"
          },
          {
            "name": "桃江",
            "code": "CN101250703",
            "name_en": "taojiang"
          },
          {
            "name": "安化",
            "code": "CN101250704",
            "name_en": "anhua"
          },
          {
            "name": "沅江",
            "code": "CN101250705",
            "name_en": "yuanjiang"
          }
        ]
      },
      {
        "name": "娄底",
        "county": [
          {
            "name": "娄底",
            "code": "CN101250801",
            "name_en": "loudi"
          },
          {
            "name": "双峰",
            "code": "CN101250802",
            "name_en": "shuangfeng"
          },
          {
            "name": "冷水江",
            "code": "CN101250803",
            "name_en": "lengshuijiang"
          },
          {
            "name": "新化",
            "code": "CN101250805",
            "name_en": "xinhua"
          },
          {
            "name": "涟源",
            "code": "CN101250806",
            "name_en": "lianyuan"
          }
        ]
      },
      {
        "name": "邵阳",
        "county": [
          {
            "name": "邵阳",
            "code": "CN101250901",
            "name_en": "shaoyang"
          },
          {
            "name": "隆回",
            "code": "CN101250902",
            "name_en": "longhui"
          },
          {
            "name": "洞口",
            "code": "CN101250903",
            "name_en": "dongkou"
          },
          {
            "name": "新邵",
            "code": "CN101250904",
            "name_en": "xinshao"
          },
          {
            "name": "邵东",
            "code": "CN101250905",
            "name_en": "shaodong"
          },
          {
            "name": "绥宁",
            "code": "CN101250906",
            "name_en": "suining"
          },
          {
            "name": "新宁",
            "code": "CN101250907",
            "name_en": "xinning"
          },
          {
            "name": "武冈",
            "code": "CN101250908",
            "name_en": "wugang"
          },
          {
            "name": "城步",
            "code": "CN101250909",
            "name_en": "chengbu"
          },
          {
            "name": "邵阳县",
            "code": "CN101250910",
            "name_en": "shaoyangxian"
          }
        ]
      },
      {
        "name": "岳阳",
        "county": [
          {
            "name": "岳阳",
            "code": "CN101251001",
            "name_en": "yueyang"
          },
          {
            "name": "华容",
            "code": "CN101251002",
            "name_en": "huarong"
          },
          {
            "name": "湘阴",
            "code": "CN101251003",
            "name_en": "xiangyin"
          },
          {
            "name": "汨罗",
            "code": "CN101251004",
            "name_en": "miluo"
          },
          {
            "name": "平江",
            "code": "CN101251005",
            "name_en": "pingjiang"
          },
          {
            "name": "临湘",
            "code": "CN101251006",
            "name_en": "linxiang"
          }
        ]
      },
      {
        "name": "张家界",
        "county": [
          {
            "name": "张家界",
            "code": "CN101251101",
            "name_en": "zhangjiajie"
          },
          {
            "name": "桑植",
            "code": "CN101251102",
            "name_en": "sangzhi"
          },
          {
            "name": "慈利",
            "code": "CN101251103",
            "name_en": "cili"
          },
          {
            "name": "武陵源",
            "code": "CN101251104",
            "name_en": "wulingyuan"
          }
        ]
      },
      {
        "name": "怀化",
        "county": [
          {
            "name": "怀化",
            "code": "CN101251201",
            "name_en": "huaihua"
          },
          {
            "name": "沅陵",
            "code": "CN101251203",
            "name_en": "yuanling"
          },
          {
            "name": "辰溪",
            "code": "CN101251204",
            "name_en": "chenxi"
          },
          {
            "name": "靖州",
            "code": "CN101251205",
            "name_en": "jingzhou"
          },
          {
            "name": "会同",
            "code": "CN101251206",
            "name_en": "huitong"
          },
          {
            "name": "通道",
            "code": "CN101251207",
            "name_en": "tongdao"
          },
          {
            "name": "麻阳",
            "code": "CN101251208",
            "name_en": "mayang"
          },
          {
            "name": "新晃",
            "code": "CN101251209",
            "name_en": "xinhuang"
          },
          {
            "name": "芷江",
            "code": "CN101251210",
            "name_en": "zhijiang"
          },
          {
            "name": "溆浦",
            "code": "CN101251211",
            "name_en": "xupu"
          },
          {
            "name": "中方",
            "code": "CN101251212",
            "name_en": "zhongfang"
          },
          {
            "name": "洪江",
            "code": "CN101251213",
            "name_en": "hongjiang"
          }
        ]
      },
      {
        "name": "永州",
        "county": [
          {
            "name": "永州",
            "code": "CN101251401",
            "name_en": "yongzhou"
          },
          {
            "name": "祁阳",
            "code": "CN101251402",
            "name_en": "qiyang"
          },
          {
            "name": "东安",
            "code": "CN101251403",
            "name_en": "dongan"
          },
          {
            "name": "双牌",
            "code": "CN101251404",
            "name_en": "shuangpai"
          },
          {
            "name": "道县",
            "code": "CN101251405",
            "name_en": "daoxian"
          },
          {
            "name": "宁远",
            "code": "CN101251406",
            "name_en": "ningyuan"
          },
          {
            "name": "江永",
            "code": "CN101251407",
            "name_en": "jiangyong"
          },
          {
            "name": "蓝山",
            "code": "CN101251408",
            "name_en": "lanshan"
          },
          {
            "name": "新田",
            "code": "CN101251409",
            "name_en": "xintian"
          },
          {
            "name": "江华",
            "code": "CN101251410",
            "name_en": "jianghua"
          },
          {
            "name": "冷水滩",
            "code": "CN101251411",
            "name_en": "lengshuitan"
          }
        ]
      },
      {
        "name": "湘西",
        "county": [
          {
            "name": "吉首",
            "code": "CN101251501",
            "name_en": "jishou"
          },
          {
            "name": "保靖",
            "code": "CN101251502",
            "name_en": "baojing"
          },
          {
            "name": "永顺",
            "code": "CN101251503",
            "name_en": "yongshun"
          },
          {
            "name": "古丈",
            "code": "CN101251504",
            "name_en": "guzhang"
          },
          {
            "name": "凤凰",
            "code": "CN101251505",
            "name_en": "fenghuang"
          },
          {
            "name": "泸溪",
            "code": "CN101251506",
            "name_en": "luxi"
          },
          {
            "name": "龙山",
            "code": "CN101251507",
            "name_en": "longshan"
          },
          {
            "name": "花垣",
            "code": "CN101251508",
            "name_en": "huayuan"
          }
        ]
      }
    ]
  },
  {
    "name": "贵州",
    "name_en": "guizhou",
    "city": [
      {
        "name": "贵阳",
        "county": [
          {
            "name": "贵阳",
            "code": "CN101260101",
            "name_en": "guiyang"
          },
          {
            "name": "白云",
            "code": "CN101260102",
            "name_en": "baiyun"
          },
          {
            "name": "花溪",
            "code": "CN101260103",
            "name_en": "huaxi"
          },
          {
            "name": "乌当",
            "code": "CN101260104",
            "name_en": "wudang"
          },
          {
            "name": "息烽",
            "code": "CN101260105",
            "name_en": "xifeng"
          },
          {
            "name": "开阳",
            "code": "CN101260106",
            "name_en": "kaiyang"
          },
          {
            "name": "修文",
            "code": "CN101260107",
            "name_en": "xiuwen"
          },
          {
            "name": "清镇",
            "code": "CN101260108",
            "name_en": "qingzhen"
          },
          {
            "name": "小河",
            "code": "CN101260109",
            "name_en": "xiaohe"
          },
          {
            "name": "云岩",
            "code": "CN101260110",
            "name_en": "yunyan"
          },
          {
            "name": "南明",
            "code": "CN101260111",
            "name_en": "nanming"
          }
        ]
      },
      {
        "name": "遵义",
        "county": [
          {
            "name": "遵义",
            "code": "CN101260201",
            "name_en": "zunyi"
          },
          {
            "name": "遵义县",
            "code": "CN101260202",
            "name_en": "zunyixian"
          },
          {
            "name": "仁怀",
            "code": "CN101260203",
            "name_en": "renhuai"
          },
          {
            "name": "绥阳",
            "code": "CN101260204",
            "name_en": "suiyang"
          },
          {
            "name": "湄潭",
            "code": "CN101260205",
            "name_en": "meitan"
          },
          {
            "name": "凤冈",
            "code": "CN101260206",
            "name_en": "fenggang"
          },
          {
            "name": "桐梓",
            "code": "CN101260207",
            "name_en": "tongzi"
          },
          {
            "name": "赤水",
            "code": "CN101260208",
            "name_en": "chishui"
          },
          {
            "name": "习水",
            "code": "CN101260209",
            "name_en": "xishui"
          },
          {
            "name": "道真",
            "code": "CN101260210",
            "name_en": "daozhen"
          },
          {
            "name": "正安",
            "code": "CN101260211",
            "name_en": "zhengan"
          },
          {
            "name": "务川",
            "code": "CN101260212",
            "name_en": "wuchuan"
          },
          {
            "name": "余庆",
            "code": "CN101260213",
            "name_en": "yuqing"
          },
          {
            "name": "汇川",
            "code": "CN101260214",
            "name_en": "huichuan"
          },
          {
            "name": "红花岗",
            "code": "CN101260215",
            "name_en": "honghuagang"
          }
        ]
      },
      {
        "name": "安顺",
        "county": [
          {
            "name": "安顺",
            "code": "CN101260301",
            "name_en": "anshun"
          },
          {
            "name": "普定",
            "code": "CN101260302",
            "name_en": "puding"
          },
          {
            "name": "镇宁",
            "code": "CN101260303",
            "name_en": "zhenning"
          },
          {
            "name": "平坝",
            "code": "CN101260304",
            "name_en": "pingba"
          },
          {
            "name": "紫云",
            "code": "CN101260305",
            "name_en": "ziyun"
          },
          {
            "name": "关岭",
            "code": "CN101260306",
            "name_en": "guanling"
          }
        ]
      },
      {
        "name": "黔南",
        "county": [
          {
            "name": "都匀",
            "code": "CN101260401",
            "name_en": "duyun"
          },
          {
            "name": "贵定",
            "code": "CN101260402",
            "name_en": "guiding"
          },
          {
            "name": "瓮安",
            "code": "CN101260403",
            "name_en": "wengan"
          },
          {
            "name": "长顺",
            "code": "CN101260404",
            "name_en": "changshun"
          },
          {
            "name": "福泉",
            "code": "CN101260405",
            "name_en": "fuquan"
          },
          {
            "name": "惠水",
            "code": "CN101260406",
            "name_en": "huishui"
          },
          {
            "name": "龙里",
            "code": "CN101260407",
            "name_en": "longli"
          },
          {
            "name": "罗甸",
            "code": "CN101260408",
            "name_en": "luodian"
          },
          {
            "name": "平塘",
            "code": "CN101260409",
            "name_en": "pingtang"
          },
          {
            "name": "独山",
            "code": "CN101260410",
            "name_en": "dushan"
          },
          {
            "name": "三都",
            "code": "CN101260411",
            "name_en": "sandu"
          },
          {
            "name": "荔波",
            "code": "CN101260412",
            "name_en": "libo"
          }
        ]
      },
      {
        "name": "黔东南",
        "county": [
          {
            "name": "凯里",
            "code": "CN101260501",
            "name_en": "kaili"
          },
          {
            "name": "岑巩",
            "code": "CN101260502",
            "name_en": "cengong"
          },
          {
            "name": "施秉",
            "code": "CN101260503",
            "name_en": "shibing"
          },
          {
            "name": "镇远",
            "code": "CN101260504",
            "name_en": "zhenyuan"
          },
          {
            "name": "黄平",
            "code": "CN101260505",
            "name_en": "huangping"
          },
          {
            "name": "麻江",
            "code": "CN101260507",
            "name_en": "majiang"
          },
          {
            "name": "丹寨",
            "code": "CN101260508",
            "name_en": "danzhai"
          },
          {
            "name": "三穗",
            "code": "CN101260509",
            "name_en": "sansui"
          },
          {
            "name": "台江",
            "code": "CN101260510",
            "name_en": "taijiang"
          },
          {
            "name": "剑河",
            "code": "CN101260511",
            "name_en": "jianhe"
          },
          {
            "name": "雷山",
            "code": "CN101260512",
            "name_en": "leishan"
          },
          {
            "name": "黎平",
            "code": "CN101260513",
            "name_en": "liping"
          },
          {
            "name": "天柱",
            "code": "CN101260514",
            "name_en": "tianzhu"
          },
          {
            "name": "锦屏",
            "code": "CN101260515",
            "name_en": "jinping"
          },
          {
            "name": "榕江",
            "code": "CN101260516",
            "name_en": "rongjiang"
          },
          {
            "name": "从江",
            "code": "CN101260517",
            "name_en": "congjiang"
          }
        ]
      },
      {
        "name": "铜仁",
        "county": [
          {
            "name": "铜仁",
            "code": "CN101260601",
            "name_en": "tongren"
          },
          {
            "name": "江口",
            "code": "CN101260602",
            "name_en": "jiangkou"
          },
          {
            "name": "玉屏",
            "code": "CN101260603",
            "name_en": "yuping"
          },
          {
            "name": "万山",
            "code": "CN101260604",
            "name_en": "wanshan"
          },
          {
            "name": "思南",
            "code": "CN101260605",
            "name_en": "sinan"
          },
          {
            "name": "印江",
            "code": "CN101260607",
            "name_en": "yinjiang"
          },
          {
            "name": "石阡",
            "code": "CN101260608",
            "name_en": "shiqian"
          },
          {
            "name": "沿河",
            "code": "CN101260609",
            "name_en": "yanhe"
          },
          {
            "name": "德江",
            "code": "CN101260610",
            "name_en": "dejiang"
          },
          {
            "name": "松桃",
            "code": "CN101260611",
            "name_en": "songtao"
          }
        ]
      },
      {
        "name": "毕节",
        "county": [
          {
            "name": "毕节",
            "code": "CN101260701",
            "name_en": "bijie"
          },
          {
            "name": "赫章",
            "code": "CN101260702",
            "name_en": "hezhang"
          },
          {
            "name": "金沙",
            "code": "CN101260703",
            "name_en": "jinsha"
          },
          {
            "name": "威宁",
            "code": "CN101260704",
            "name_en": "weining"
          },
          {
            "name": "大方",
            "code": "CN101260705",
            "name_en": "dafang"
          },
          {
            "name": "纳雍",
            "code": "CN101260706",
            "name_en": "nayong"
          },
          {
            "name": "织金",
            "code": "CN101260707",
            "name_en": "zhijin"
          },
          {
            "name": "黔西",
            "code": "CN101260708",
            "name_en": "qianxi"
          }
        ]
      },
      {
        "name": "六盘水",
        "county": [
          {
            "name": "水城",
            "code": "CN101260801",
            "name_en": "shuicheng"
          },
          {
            "name": "六枝",
            "code": "CN101260802",
            "name_en": "liuzhi"
          },
          {
            "name": "盘县",
            "code": "CN101260804",
            "name_en": "panxian"
          }
        ]
      },
      {
        "name": "黔西南",
        "county": [
          {
            "name": "兴义",
            "code": "CN101260901",
            "name_en": "xingyi"
          },
          {
            "name": "晴隆",
            "code": "CN101260902",
            "name_en": "qinglong"
          },
          {
            "name": "兴仁",
            "code": "CN101260903",
            "name_en": "xingren"
          },
          {
            "name": "贞丰",
            "code": "CN101260904",
            "name_en": "zhenfeng"
          },
          {
            "name": "望谟",
            "code": "CN101260905",
            "name_en": "wangmo"
          },
          {
            "name": "安龙",
            "code": "CN101260907",
            "name_en": "anlong"
          },
          {
            "name": "册亨",
            "code": "CN101260908",
            "name_en": "ceheng"
          },
          {
            "name": "普安",
            "code": "CN101260909",
            "name_en": "puan"
          }
        ]
      }
    ]
  },
  {
    "name": "四川",
    "name_en": "sichuan",
    "city": [
      {
        "name": "成都",
        "county": [
          {
            "name": "成都",
            "code": "CN101270101",
            "name_en": "chengdu"
          },
          {
            "name": "龙泉驿",
            "code": "CN101270102",
            "name_en": "longquanyi"
          },
          {
            "name": "新都",
            "code": "CN101270103",
            "name_en": "xindu"
          },
          {
            "name": "温江",
            "code": "CN101270104",
            "name_en": "wenjiang"
          },
          {
            "name": "金堂",
            "code": "CN101270105",
            "name_en": "jintang"
          },
          {
            "name": "双流",
            "code": "CN101270106",
            "name_en": "shuangliu"
          },
          {
            "name": "郫县",
            "code": "CN101270107",
            "name_en": "pixian"
          },
          {
            "name": "大邑",
            "code": "CN101270108",
            "name_en": "dayi"
          },
          {
            "name": "蒲江",
            "code": "CN101270109",
            "name_en": "pujiang"
          },
          {
            "name": "新津",
            "code": "CN101270110",
            "name_en": "xinjin"
          },
          {
            "name": "都江堰",
            "code": "CN101270111",
            "name_en": "dujiangyan"
          },
          {
            "name": "彭州",
            "code": "CN101270112",
            "name_en": "pengzhou"
          },
          {
            "name": "邛崃",
            "code": "CN101270113",
            "name_en": "qionglai"
          },
          {
            "name": "崇州",
            "code": "CN101270114",
            "name_en": "chongzhou"
          },
          {
            "name": "青白江",
            "code": "CN101270115",
            "name_en": "qingbaijiang"
          }
        ]
      },
      {
        "name": "攀枝花",
        "county": [
          {
            "name": "攀枝花",
            "code": "CN101270201",
            "name_en": "panzhihua"
          },
          {
            "name": "仁和",
            "code": "CN101270202",
            "name_en": "renhe"
          },
          {
            "name": "米易",
            "code": "CN101270203",
            "name_en": "miyi"
          },
          {
            "name": "盐边",
            "code": "CN101270204",
            "name_en": "yanbian"
          }
        ]
      },
      {
        "name": "自贡",
        "county": [
          {
            "name": "自贡",
            "code": "CN101270301",
            "name_en": "zigong"
          },
          {
            "name": "富顺",
            "code": "CN101270302",
            "name_en": "fushun"
          },
          {
            "name": "荣县",
            "code": "CN101270303",
            "name_en": "rongxian"
          }
        ]
      },
      {
        "name": "绵阳",
        "county": [
          {
            "name": "绵阳",
            "code": "CN101270401",
            "name_en": "mianyang"
          },
          {
            "name": "三台",
            "code": "CN101270402",
            "name_en": "santai"
          },
          {
            "name": "盐亭",
            "code": "CN101270403",
            "name_en": "yanting"
          },
          {
            "name": "安县",
            "code": "CN101270404",
            "name_en": "anxian"
          },
          {
            "name": "梓潼",
            "code": "CN101270405",
            "name_en": "zitong"
          },
          {
            "name": "北川",
            "code": "CN101270406",
            "name_en": "beichuan"
          },
          {
            "name": "平武",
            "code": "CN101270407",
            "name_en": "pingwu"
          },
          {
            "name": "江油",
            "code": "CN101270408",
            "name_en": "jiangyou"
          }
        ]
      },
      {
        "name": "南充",
        "county": [
          {
            "name": "南充",
            "code": "CN101270501",
            "name_en": "nanchong"
          },
          {
            "name": "南部",
            "code": "CN101270502",
            "name_en": "nanbu"
          },
          {
            "name": "营山",
            "code": "CN101270503",
            "name_en": "yingshan"
          },
          {
            "name": "蓬安",
            "code": "CN101270504",
            "name_en": "pengan"
          },
          {
            "name": "仪陇",
            "code": "CN101270505",
            "name_en": "yilong"
          },
          {
            "name": "西充",
            "code": "CN101270506",
            "name_en": "xichong"
          },
          {
            "name": "阆中",
            "code": "CN101270507",
            "name_en": "langzhong"
          }
        ]
      },
      {
        "name": "达州",
        "county": [
          {
            "name": "达州",
            "code": "CN101270601",
            "name_en": "dazhou"
          },
          {
            "name": "宣汉",
            "code": "CN101270602",
            "name_en": "xuanhan"
          },
          {
            "name": "开江",
            "code": "CN101270603",
            "name_en": "kaijiang"
          },
          {
            "name": "大竹",
            "code": "CN101270604",
            "name_en": "dazhu"
          },
          {
            "name": "渠县",
            "code": "CN101270605",
            "name_en": "quxian"
          },
          {
            "name": "万源",
            "code": "CN101270606",
            "name_en": "wanyuan"
          },
          {
            "name": "通川",
            "code": "CN101270607",
            "name_en": "tongchuan"
          },
          {
            "name": "达县",
            "code": "CN101270608",
            "name_en": "daxian"
          }
        ]
      },
      {
        "name": "遂宁",
        "county": [
          {
            "name": "遂宁",
            "code": "CN101270701",
            "name_en": "suining"
          },
          {
            "name": "蓬溪",
            "code": "CN101270702",
            "name_en": "pengxi"
          },
          {
            "name": "射洪",
            "code": "CN101270703",
            "name_en": "shehong"
          }
        ]
      },
      {
        "name": "广安",
        "county": [
          {
            "name": "广安",
            "code": "CN101270801",
            "name_en": "guangan"
          },
          {
            "name": "岳池",
            "code": "CN101270802",
            "name_en": "yuechi"
          },
          {
            "name": "武胜",
            "code": "CN101270803",
            "name_en": "wusheng"
          },
          {
            "name": "邻水",
            "code": "CN101270804",
            "name_en": "linshui"
          },
          {
            "name": "华蓥",
            "code": "CN101270805",
            "name_en": "huaying"
          }
        ]
      },
      {
        "name": "巴中",
        "county": [
          {
            "name": "巴中",
            "code": "CN101270901",
            "name_en": "bazhong"
          },
          {
            "name": "通江",
            "code": "CN101270902",
            "name_en": "tongjiang"
          },
          {
            "name": "南江",
            "code": "CN101270903",
            "name_en": "nanjiang"
          },
          {
            "name": "平昌",
            "code": "CN101270904",
            "name_en": "pingchang"
          }
        ]
      },
      {
        "name": "泸州",
        "county": [
          {
            "name": "泸州",
            "code": "CN101271001",
            "name_en": "luzhou"
          },
          {
            "name": "泸县",
            "code": "CN101271003",
            "name_en": "luxian"
          },
          {
            "name": "合江",
            "code": "CN101271004",
            "name_en": "hejiang"
          },
          {
            "name": "叙永",
            "code": "CN101271005",
            "name_en": "xuyong"
          },
          {
            "name": "古蔺",
            "code": "CN101271006",
            "name_en": "gulin"
          },
          {
            "name": "纳溪",
            "code": "CN101271007",
            "name_en": "naxi"
          }
        ]
      },
      {
        "name": "宜宾",
        "county": [
          {
            "name": "宜宾",
            "code": "CN101271101",
            "name_en": "yibin"
          },
          {
            "name": "宜宾县",
            "code": "CN101271103",
            "name_en": "yibinxian"
          },
          {
            "name": "南溪",
            "code": "CN101271104",
            "name_en": "nanxi"
          },
          {
            "name": "江安",
            "code": "CN101271105",
            "name_en": "jiangan"
          },
          {
            "name": "长宁",
            "code": "CN101271106",
            "name_en": "changning"
          },
          {
            "name": "高县",
            "code": "CN101271107",
            "name_en": "gaoxian"
          },
          {
            "name": "珙县",
            "code": "CN101271108",
            "name_en": "gongxian"
          },
          {
            "name": "筠连",
            "code": "CN101271109",
            "name_en": "junlian"
          },
          {
            "name": "兴文",
            "code": "CN101271110",
            "name_en": "xingwen"
          },
          {
            "name": "屏山",
            "code": "CN101271111",
            "name_en": "pingshan"
          }
        ]
      },
      {
        "name": "内江",
        "county": [
          {
            "name": "内江",
            "code": "CN101271201",
            "name_en": "neijiang"
          },
          {
            "name": "东兴",
            "code": "CN101271202",
            "name_en": "dongxing"
          },
          {
            "name": "威远",
            "code": "CN101271203",
            "name_en": "weiyuan"
          },
          {
            "name": "资中",
            "code": "CN101271204",
            "name_en": "zizhong"
          },
          {
            "name": "隆昌",
            "code": "CN101271205",
            "name_en": "longchang"
          }
        ]
      },
      {
        "name": "资阳",
        "county": [
          {
            "name": "资阳",
            "code": "CN101271301",
            "name_en": "ziyang"
          },
          {
            "name": "安岳",
            "code": "CN101271302",
            "name_en": "anyue"
          },
          {
            "name": "乐至",
            "code": "CN101271303",
            "name_en": "lezhi"
          },
          {
            "name": "简阳",
            "code": "CN101271304",
            "name_en": "jianyang"
          }
        ]
      },
      {
        "name": "乐山",
        "county": [
          {
            "name": "乐山",
            "code": "CN101271401",
            "name_en": "leshan"
          },
          {
            "name": "犍为",
            "code": "CN101271402",
            "name_en": "qianwei"
          },
          {
            "name": "井研",
            "code": "CN101271403",
            "name_en": "jingyan"
          },
          {
            "name": "夹江",
            "code": "CN101271404",
            "name_en": "jiajiang"
          },
          {
            "name": "沐川",
            "code": "CN101271405",
            "name_en": "muchuan"
          },
          {
            "name": "峨边",
            "code": "CN101271406",
            "name_en": "ebian"
          },
          {
            "name": "马边",
            "code": "CN101271407",
            "name_en": "mabian"
          },
          {
            "name": "峨眉",
            "code": "CN101271408",
            "name_en": "emei"
          },
          {
            "name": "峨眉山",
            "code": "CN101271409",
            "name_en": "emeishan"
          }
        ]
      },
      {
        "name": "眉山",
        "county": [
          {
            "name": "眉山",
            "code": "CN101271501",
            "name_en": "meishan"
          },
          {
            "name": "仁寿",
            "code": "CN101271502",
            "name_en": "renshou"
          },
          {
            "name": "彭山",
            "code": "CN101271503",
            "name_en": "pengshan"
          },
          {
            "name": "洪雅",
            "code": "CN101271504",
            "name_en": "hongya"
          },
          {
            "name": "丹棱",
            "code": "CN101271505",
            "name_en": "danleng"
          },
          {
            "name": "青神",
            "code": "CN101271506",
            "name_en": "qingshen"
          }
        ]
      },
      {
        "name": "凉山",
        "county": [
          {
            "name": "凉山",
            "code": "CN101271601",
            "name_en": "liangshan"
          },
          {
            "name": "木里",
            "code": "CN101271603",
            "name_en": "muli"
          },
          {
            "name": "盐源",
            "code": "CN101271604",
            "name_en": "yanyuan"
          },
          {
            "name": "德昌",
            "code": "CN101271605",
            "name_en": "dechang"
          },
          {
            "name": "会理",
            "code": "CN101271606",
            "name_en": "huili"
          },
          {
            "name": "会东",
            "code": "CN101271607",
            "name_en": "huidong"
          },
          {
            "name": "宁南",
            "code": "CN101271608",
            "name_en": "ningnan"
          },
          {
            "name": "普格",
            "code": "CN101271609",
            "name_en": "puge"
          },
          {
            "name": "西昌",
            "code": "CN101271610",
            "name_en": "xichang"
          },
          {
            "name": "金阳",
            "code": "CN101271611",
            "name_en": "jinyang"
          },
          {
            "name": "昭觉",
            "code": "CN101271612",
            "name_en": "zhaojue"
          },
          {
            "name": "喜德",
            "code": "CN101271613",
            "name_en": "xide"
          },
          {
            "name": "冕宁",
            "code": "CN101271614",
            "name_en": "mianning"
          },
          {
            "name": "越西",
            "code": "CN101271615",
            "name_en": "yuexi"
          },
          {
            "name": "甘洛",
            "code": "CN101271616",
            "name_en": "ganluo"
          },
          {
            "name": "雷波",
            "code": "CN101271617",
            "name_en": "leibo"
          },
          {
            "name": "美姑",
            "code": "CN101271618",
            "name_en": "meigu"
          },
          {
            "name": "布拖",
            "code": "CN101271619",
            "name_en": "butuo"
          }
        ]
      },
      {
        "name": "雅安",
        "county": [
          {
            "name": "雅安",
            "code": "CN101271701",
            "name_en": "yaan"
          },
          {
            "name": "名山",
            "code": "CN101271702",
            "name_en": "mingshan"
          },
          {
            "name": "荥经",
            "code": "CN101271703",
            "name_en": "yingjing"
          },
          {
            "name": "汉源",
            "code": "CN101271704",
            "name_en": "hanyuan"
          },
          {
            "name": "石棉",
            "code": "CN101271705",
            "name_en": "shimian"
          },
          {
            "name": "天全",
            "code": "CN101271706",
            "name_en": "tianquan"
          },
          {
            "name": "芦山",
            "code": "CN101271707",
            "name_en": "lushan"
          },
          {
            "name": "宝兴",
            "code": "CN101271708",
            "name_en": "baoxing"
          }
        ]
      },
      {
        "name": "甘孜",
        "county": [
          {
            "name": "甘孜",
            "code": "CN101271801",
            "name_en": "ganzi"
          },
          {
            "name": "康定",
            "code": "CN101271802",
            "name_en": "kangding"
          },
          {
            "name": "泸定",
            "code": "CN101271803",
            "name_en": "luding"
          },
          {
            "name": "丹巴",
            "code": "CN101271804",
            "name_en": "danba"
          },
          {
            "name": "九龙",
            "code": "CN101271805",
            "name_en": "jiulong"
          },
          {
            "name": "雅江",
            "code": "CN101271806",
            "name_en": "yajiang"
          },
          {
            "name": "道孚",
            "code": "CN101271807",
            "name_en": "daofu"
          },
          {
            "name": "炉霍",
            "code": "CN101271808",
            "name_en": "luhuo"
          },
          {
            "name": "新龙",
            "code": "CN101271809",
            "name_en": "xinlong"
          },
          {
            "name": "德格",
            "code": "CN101271810",
            "name_en": "dege"
          },
          {
            "name": "白玉",
            "code": "CN101271811",
            "name_en": "baiyu"
          },
          {
            "name": "石渠",
            "code": "CN101271812",
            "name_en": "shiqu"
          },
          {
            "name": "色达",
            "code": "CN101271813",
            "name_en": "seda"
          },
          {
            "name": "理塘",
            "code": "CN101271814",
            "name_en": "litang"
          },
          {
            "name": "巴塘",
            "code": "CN101271815",
            "name_en": "batang"
          },
          {
            "name": "乡城",
            "code": "CN101271816",
            "name_en": "xiangcheng"
          },
          {
            "name": "稻城",
            "code": "CN101271817",
            "name_en": "daocheng"
          },
          {
            "name": "得荣",
            "code": "CN101271818",
            "name_en": "derong"
          }
        ]
      },
      {
        "name": "阿坝",
        "county": [
          {
            "name": "阿坝",
            "code": "CN101271901",
            "name_en": "aba"
          },
          {
            "name": "汶川",
            "code": "CN101271902",
            "name_en": "wenchuan"
          },
          {
            "name": "理县",
            "code": "CN101271903",
            "name_en": "lixian"
          },
          {
            "name": "茂县",
            "code": "CN101271904",
            "name_en": "maoxian"
          },
          {
            "name": "松潘",
            "code": "CN101271905",
            "name_en": "songfan"
          },
          {
            "name": "九寨沟",
            "code": "CN101271906",
            "name_en": "jiuzhaigou"
          },
          {
            "name": "金川",
            "code": "CN101271907",
            "name_en": "jinchuan"
          },
          {
            "name": "小金",
            "code": "CN101271908",
            "name_en": "xiaojin"
          },
          {
            "name": "黑水",
            "code": "CN101271909",
            "name_en": "heishui"
          },
          {
            "name": "马尔康",
            "code": "CN101271910",
            "name_en": "maerkang"
          },
          {
            "name": "壤塘",
            "code": "CN101271911",
            "name_en": "rangtang"
          },
          {
            "name": "若尔盖",
            "code": "CN101271912",
            "name_en": "nuoergai"
          },
          {
            "name": "红原",
            "code": "CN101271913",
            "name_en": "hongyuan"
          }
        ]
      },
      {
        "name": "德阳",
        "county": [
          {
            "name": "德阳",
            "code": "CN101272001",
            "name_en": "deyang"
          },
          {
            "name": "中江",
            "code": "CN101272002",
            "name_en": "zhongjiang"
          },
          {
            "name": "广汉",
            "code": "CN101272003",
            "name_en": "guanghan"
          },
          {
            "name": "什邡",
            "code": "CN101272004",
            "name_en": "shifang"
          },
          {
            "name": "绵竹",
            "code": "CN101272005",
            "name_en": "mianzhu"
          },
          {
            "name": "罗江",
            "code": "CN101272006",
            "name_en": "luojiang"
          }
        ]
      },
      {
        "name": "广元",
        "county": [
          {
            "name": "广元",
            "code": "CN101272101",
            "name_en": "guangyuan"
          },
          {
            "name": "旺苍",
            "code": "CN101272102",
            "name_en": "wangcang"
          },
          {
            "name": "青川",
            "code": "CN101272103",
            "name_en": "qingchuan"
          },
          {
            "name": "剑阁",
            "code": "CN101272104",
            "name_en": "jiange"
          },
          {
            "name": "苍溪",
            "code": "CN101272105",
            "name_en": "cangxi"
          }
        ]
      }
    ]
  },
  {
    "name": "广东",
    "name_en": "guangdong",
    "city": [
      {
        "name": "广州",
        "county": [
          {
            "name": "广州",
            "code": "CN101280101",
            "name_en": "guangzhou"
          },
          {
            "name": "番禺",
            "code": "CN101280102",
            "name_en": "panyu"
          },
          {
            "name": "从化",
            "code": "CN101280103",
            "name_en": "conghua"
          },
          {
            "name": "增城",
            "code": "CN101280104",
            "name_en": "zengcheng"
          },
          {
            "name": "花都",
            "code": "CN101280105",
            "name_en": "huadu"
          }
        ]
      },
      {
        "name": "韶关",
        "county": [
          {
            "name": "韶关",
            "code": "CN101280201",
            "name_en": "shaoguan"
          },
          {
            "name": "乳源",
            "code": "CN101280202",
            "name_en": "ruyuan"
          },
          {
            "name": "始兴",
            "code": "CN101280203",
            "name_en": "shixing"
          },
          {
            "name": "翁源",
            "code": "CN101280204",
            "name_en": "wengyuan"
          },
          {
            "name": "乐昌",
            "code": "CN101280205",
            "name_en": "lechang"
          },
          {
            "name": "仁化",
            "code": "CN101280206",
            "name_en": "renhua"
          },
          {
            "name": "南雄",
            "code": "CN101280207",
            "name_en": "nanxiong"
          },
          {
            "name": "新丰",
            "code": "CN101280208",
            "name_en": "xinfeng"
          },
          {
            "name": "曲江",
            "code": "CN101280209",
            "name_en": "qujiang"
          },
          {
            "name": "浈江",
            "code": "CN101280210",
            "name_en": "zhenjiang"
          },
          {
            "name": "武江",
            "code": "CN101280211",
            "name_en": "wujiang"
          }
        ]
      },
      {
        "name": "惠州",
        "county": [
          {
            "name": "惠州",
            "code": "CN101280301",
            "name_en": "huizhou"
          },
          {
            "name": "博罗",
            "code": "CN101280302",
            "name_en": "boluo"
          },
          {
            "name": "惠阳",
            "code": "CN101280303",
            "name_en": "huiyang"
          },
          {
            "name": "惠东",
            "code": "CN101280304",
            "name_en": "huidong"
          },
          {
            "name": "龙门",
            "code": "CN101280305",
            "name_en": "longmen"
          }
        ]
      },
      {
        "name": "梅州",
        "county": [
          {
            "name": "梅州",
            "code": "CN101280401",
            "name_en": "meizhou"
          },
          {
            "name": "兴宁",
            "code": "CN101280402",
            "name_en": "xingning"
          },
          {
            "name": "蕉岭",
            "code": "CN101280403",
            "name_en": "jiaoling"
          },
          {
            "name": "大埔",
            "code": "CN101280404",
            "name_en": "dabu"
          },
          {
            "name": "丰顺",
            "code": "CN101280406",
            "name_en": "fengshun"
          },
          {
            "name": "平远",
            "code": "CN101280407",
            "name_en": "pingyuan"
          },
          {
            "name": "五华",
            "code": "CN101280408",
            "name_en": "wuhua"
          },
          {
            "name": "梅县",
            "code": "CN101280409",
            "name_en": "meixian"
          }
        ]
      },
      {
        "name": "汕头",
        "county": [
          {
            "name": "汕头",
            "code": "CN101280501",
            "name_en": "shantou"
          },
          {
            "name": "潮阳",
            "code": "CN101280502",
            "name_en": "chaoyang"
          },
          {
            "name": "澄海",
            "code": "CN101280503",
            "name_en": "chenghai"
          },
          {
            "name": "南澳",
            "code": "CN101280504",
            "name_en": "nanao"
          }
        ]
      },
      {
        "name": "深圳",
        "county": [
          {
            "name": "深圳",
            "code": "CN101280601",
            "name_en": "shenzhen"
          }
        ]
      },
      {
        "name": "珠海",
        "county": [
          {
            "name": "珠海",
            "code": "CN101280701",
            "name_en": "zhuhai"
          },
          {
            "name": "斗门",
            "code": "CN101280702",
            "name_en": "doumen"
          },
          {
            "name": "金湾",
            "code": "CN101280703",
            "name_en": "jinwan"
          }
        ]
      },
      {
        "name": "佛山",
        "county": [
          {
            "name": "佛山",
            "code": "CN101280800",
            "name_en": "foshan"
          },
          {
            "name": "顺德",
            "code": "CN101280801",
            "name_en": "shunde"
          },
          {
            "name": "三水",
            "code": "CN101280802",
            "name_en": "sanshui"
          },
          {
            "name": "南海",
            "code": "CN101280803",
            "name_en": "nanhai"
          },
          {
            "name": "高明",
            "code": "CN101280804",
            "name_en": "gaoming"
          }
        ]
      },
      {
        "name": "肇庆",
        "county": [
          {
            "name": "肇庆",
            "code": "CN101280901",
            "name_en": "zhaoqing"
          },
          {
            "name": "广宁",
            "code": "CN101280902",
            "name_en": "guangning"
          },
          {
            "name": "四会",
            "code": "CN101280903",
            "name_en": "sihui"
          },
          {
            "name": "德庆",
            "code": "CN101280905",
            "name_en": "deqing"
          },
          {
            "name": "怀集",
            "code": "CN101280906",
            "name_en": "huaiji"
          },
          {
            "name": "封开",
            "code": "CN101280907",
            "name_en": "fengkai"
          },
          {
            "name": "高要",
            "code": "CN101280908",
            "name_en": "gaoyao"
          }
        ]
      },
      {
        "name": "湛江",
        "county": [
          {
            "name": "湛江",
            "code": "CN101281001",
            "name_en": "zhanjiang"
          },
          {
            "name": "吴川",
            "code": "CN101281002",
            "name_en": "wuchuan"
          },
          {
            "name": "雷州",
            "code": "CN101281003",
            "name_en": "leizhou"
          },
          {
            "name": "徐闻",
            "code": "CN101281004",
            "name_en": "xuwen"
          },
          {
            "name": "廉江",
            "code": "CN101281005",
            "name_en": "lianjiang"
          },
          {
            "name": "赤坎",
            "code": "CN101281006",
            "name_en": "chikan"
          },
          {
            "name": "遂溪",
            "code": "CN101281007",
            "name_en": "suixi"
          },
          {
            "name": "坡头",
            "code": "CN101281008",
            "name_en": "potou"
          },
          {
            "name": "霞山",
            "code": "CN101281009",
            "name_en": "xiashan"
          },
          {
            "name": "麻章",
            "code": "CN101281010",
            "name_en": "mazhang"
          }
        ]
      },
      {
        "name": "江门",
        "county": [
          {
            "name": "江门",
            "code": "CN101281101",
            "name_en": "jiangmen"
          },
          {
            "name": "开平",
            "code": "CN101281103",
            "name_en": "kaiping"
          },
          {
            "name": "新会",
            "code": "CN101281104",
            "name_en": "xinhui"
          },
          {
            "name": "恩平",
            "code": "CN101281105",
            "name_en": "enping"
          },
          {
            "name": "台山",
            "code": "CN101281106",
            "name_en": "taishan"
          },
          {
            "name": "蓬江",
            "code": "CN101281107",
            "name_en": "pengjiang"
          },
          {
            "name": "鹤山",
            "code": "CN101281108",
            "name_en": "heshan"
          },
          {
            "name": "江海",
            "code": "CN101281109",
            "name_en": "jianghai"
          }
        ]
      },
      {
        "name": "河源",
        "county": [
          {
            "name": "河源",
            "code": "CN101281201",
            "name_en": "heyuan"
          },
          {
            "name": "紫金",
            "code": "CN101281202",
            "name_en": "zijin"
          },
          {
            "name": "连平",
            "code": "CN101281203",
            "name_en": "lianping"
          },
          {
            "name": "和平",
            "code": "CN101281204",
            "name_en": "heping"
          },
          {
            "name": "龙川",
            "code": "CN101281205",
            "name_en": "longchuan"
          },
          {
            "name": "东源",
            "code": "CN101281206",
            "name_en": "dongyuan"
          }
        ]
      },
      {
        "name": "清远",
        "county": [
          {
            "name": "清远",
            "code": "CN101281301",
            "name_en": "qingyuan"
          },
          {
            "name": "连南",
            "code": "CN101281302",
            "name_en": "liannan"
          },
          {
            "name": "连州",
            "code": "CN101281303",
            "name_en": "lianzhou"
          },
          {
            "name": "连山",
            "code": "CN101281304",
            "name_en": "lianshan"
          },
          {
            "name": "阳山",
            "code": "CN101281305",
            "name_en": "yangshan"
          },
          {
            "name": "佛冈",
            "code": "CN101281306",
            "name_en": "fogang"
          },
          {
            "name": "英德",
            "code": "CN101281307",
            "name_en": "yingde"
          },
          {
            "name": "清新",
            "code": "CN101281308",
            "name_en": "qingxin"
          }
        ]
      },
      {
        "name": "云浮",
        "county": [
          {
            "name": "云浮",
            "code": "CN101281401",
            "name_en": "yunfu"
          },
          {
            "name": "罗定",
            "code": "CN101281402",
            "name_en": "luoding"
          },
          {
            "name": "新兴",
            "code": "CN101281403",
            "name_en": "xinxing"
          },
          {
            "name": "郁南",
            "code": "CN101281404",
            "name_en": "yunan"
          },
          {
            "name": "云安",
            "code": "CN101281406",
            "name_en": "yunan"
          }
        ]
      },
      {
        "name": "潮州",
        "county": [
          {
            "name": "潮州",
            "code": "CN101281501",
            "name_en": "chaozhou"
          },
          {
            "name": "饶平",
            "code": "CN101281502",
            "name_en": "raoping"
          },
          {
            "name": "潮安",
            "code": "CN101281503",
            "name_en": "chaoan"
          }
        ]
      },
      {
        "name": "东莞",
        "county": [
          {
            "name": "东莞",
            "code": "CN101281601",
            "name_en": "dongguan"
          }
        ]
      },
      {
        "name": "中山",
        "county": [
          {
            "name": "中山",
            "code": "CN101281701",
            "name_en": "zhongshan"
          }
        ]
      },
      {
        "name": "阳江",
        "county": [
          {
            "name": "阳江",
            "code": "CN101281801",
            "name_en": "yangjiang"
          },
          {
            "name": "阳春",
            "code": "CN101281802",
            "name_en": "yangchun"
          },
          {
            "name": "阳东",
            "code": "CN101281803",
            "name_en": "yangdong"
          },
          {
            "name": "阳西",
            "code": "CN101281804",
            "name_en": "yangxi"
          }
        ]
      },
      {
        "name": "揭阳",
        "county": [
          {
            "name": "揭阳",
            "code": "CN101281901",
            "name_en": "jieyang"
          },
          {
            "name": "揭西",
            "code": "CN101281902",
            "name_en": "jiexi"
          },
          {
            "name": "普宁",
            "code": "CN101281903",
            "name_en": "puning"
          },
          {
            "name": "惠来",
            "code": "CN101281904",
            "name_en": "huilai"
          },
          {
            "name": "揭东",
            "code": "CN101281905",
            "name_en": "jiedong"
          }
        ]
      },
      {
        "name": "茂名",
        "county": [
          {
            "name": "茂名",
            "code": "CN101282001",
            "name_en": "maoming"
          },
          {
            "name": "高州",
            "code": "CN101282002",
            "name_en": "gaozhou"
          },
          {
            "name": "化州",
            "code": "CN101282003",
            "name_en": "huazhou"
          },
          {
            "name": "电白",
            "code": "CN101282004",
            "name_en": "dianbai"
          },
          {
            "name": "信宜",
            "code": "CN101282005",
            "name_en": "xinyi"
          },
          {
            "name": "茂港",
            "code": "CN101282006",
            "name_en": "maogang"
          }
        ]
      },
      {
        "name": "汕尾",
        "county": [
          {
            "name": "汕尾",
            "code": "CN101282101",
            "name_en": "shanwei"
          },
          {
            "name": "海丰",
            "code": "CN101282102",
            "name_en": "haifeng"
          },
          {
            "name": "陆丰",
            "code": "CN101282103",
            "name_en": "lufeng"
          },
          {
            "name": "陆河",
            "code": "CN101282104",
            "name_en": "luhe"
          }
        ]
      }
    ]
  },
  {
    "name": "云南",
    "name_en": "yunnan",
    "city": [
      {
        "name": "昆明",
        "county": [
          {
            "name": "昆明",
            "code": "CN101290101",
            "name_en": "kunming"
          },
          {
            "name": "东川",
            "code": "CN101290103",
            "name_en": "dongchuan"
          },
          {
            "name": "寻甸",
            "code": "CN101290104",
            "name_en": "xundian"
          },
          {
            "name": "晋宁",
            "code": "CN101290105",
            "name_en": "jinning"
          },
          {
            "name": "宜良",
            "code": "CN101290106",
            "name_en": "yiliang"
          },
          {
            "name": "石林",
            "code": "CN101290107",
            "name_en": "shilin"
          },
          {
            "name": "呈贡",
            "code": "CN101290108",
            "name_en": "chenggong"
          },
          {
            "name": "富民",
            "code": "CN101290109",
            "name_en": "fumin"
          },
          {
            "name": "嵩明",
            "code": "CN101290110",
            "name_en": "songming"
          },
          {
            "name": "禄劝",
            "code": "CN101290111",
            "name_en": "luquan"
          },
          {
            "name": "安宁",
            "code": "CN101290112",
            "name_en": "anning"
          },
          {
            "name": "太华山",
            "code": "CN101290113",
            "name_en": "taihuashan"
          }
        ]
      },
      {
        "name": "大理",
        "county": [
          {
            "name": "大理",
            "code": "CN101290201",
            "name_en": "dali"
          },
          {
            "name": "云龙",
            "code": "CN101290202",
            "name_en": "yunlong"
          },
          {
            "name": "漾濞",
            "code": "CN101290203",
            "name_en": "yangbi"
          },
          {
            "name": "永平",
            "code": "CN101290204",
            "name_en": "yongping"
          },
          {
            "name": "宾川",
            "code": "CN101290205",
            "name_en": "binchuan"
          },
          {
            "name": "弥渡",
            "code": "CN101290206",
            "name_en": "midu"
          },
          {
            "name": "祥云",
            "code": "CN101290207",
            "name_en": "xiangyun"
          },
          {
            "name": "巍山",
            "code": "CN101290208",
            "name_en": "weishan"
          },
          {
            "name": "剑川",
            "code": "CN101290209",
            "name_en": "jianchuan"
          },
          {
            "name": "洱源",
            "code": "CN101290210",
            "name_en": "eryuan"
          },
          {
            "name": "鹤庆",
            "code": "CN101290211",
            "name_en": "heqing"
          },
          {
            "name": "南涧",
            "code": "CN101290212",
            "name_en": "nanjian"
          }
        ]
      },
      {
        "name": "红河",
        "county": [
          {
            "name": "红河",
            "code": "CN101290301",
            "name_en": "honghe"
          },
          {
            "name": "石屏",
            "code": "CN101290302",
            "name_en": "shiping"
          },
          {
            "name": "建水",
            "code": "CN101290303",
            "name_en": "jianshui"
          },
          {
            "name": "弥勒",
            "code": "CN101290304",
            "name_en": "mile"
          },
          {
            "name": "元阳",
            "code": "CN101290305",
            "name_en": "yuanyang"
          },
          {
            "name": "绿春",
            "code": "CN101290306",
            "name_en": "lvchun"
          },
          {
            "name": "开远",
            "code": "CN101290307",
            "name_en": "kaiyuan"
          },
          {
            "name": "个旧",
            "code": "CN101290308",
            "name_en": "gejiu"
          },
          {
            "name": "蒙自",
            "code": "CN101290309",
            "name_en": "mengzi"
          },
          {
            "name": "屏边",
            "code": "CN101290310",
            "name_en": "pingbian"
          },
          {
            "name": "泸西",
            "code": "CN101290311",
            "name_en": "luxi"
          },
          {
            "name": "金平",
            "code": "CN101290312",
            "name_en": "jinping"
          },
          {
            "name": "河口",
            "code": "CN101290313",
            "name_en": "hekou"
          }
        ]
      },
      {
        "name": "曲靖",
        "county": [
          {
            "name": "曲靖",
            "code": "CN101290401",
            "name_en": "qujing"
          },
          {
            "name": "沾益",
            "code": "CN101290402",
            "name_en": "zhanyi"
          },
          {
            "name": "陆良",
            "code": "CN101290403",
            "name_en": "luliang"
          },
          {
            "name": "富源",
            "code": "CN101290404",
            "name_en": "fuyuan"
          },
          {
            "name": "马龙",
            "code": "CN101290405",
            "name_en": "malong"
          },
          {
            "name": "师宗",
            "code": "CN101290406",
            "name_en": "shizong"
          },
          {
            "name": "罗平",
            "code": "CN101290407",
            "name_en": "luoping"
          },
          {
            "name": "会泽",
            "code": "CN101290408",
            "name_en": "huize"
          },
          {
            "name": "宣威",
            "code": "CN101290409",
            "name_en": "xuanwei"
          }
        ]
      },
      {
        "name": "保山",
        "county": [
          {
            "name": "保山",
            "code": "CN101290501",
            "name_en": "baoshan"
          },
          {
            "name": "龙陵",
            "code": "CN101290503",
            "name_en": "longling"
          },
          {
            "name": "施甸",
            "code": "CN101290504",
            "name_en": "sidian"
          },
          {
            "name": "昌宁",
            "code": "CN101290505",
            "name_en": "changning"
          },
          {
            "name": "腾冲",
            "code": "CN101290506",
            "name_en": "tengchong"
          }
        ]
      },
      {
        "name": "文山",
        "county": [
          {
            "name": "文山",
            "code": "CN101290601",
            "name_en": "wenshan"
          },
          {
            "name": "西畴",
            "code": "CN101290602",
            "name_en": "xichou"
          },
          {
            "name": "马关",
            "code": "CN101290603",
            "name_en": "maguan"
          },
          {
            "name": "麻栗坡",
            "code": "CN101290604",
            "name_en": "malipo"
          },
          {
            "name": "砚山",
            "code": "CN101290605",
            "name_en": "yanshan"
          },
          {
            "name": "丘北",
            "code": "CN101290606",
            "name_en": "qiubei"
          },
          {
            "name": "广南",
            "code": "CN101290607",
            "name_en": "guangnan"
          },
          {
            "name": "富宁",
            "code": "CN101290608",
            "name_en": "funing"
          }
        ]
      },
      {
        "name": "玉溪",
        "county": [
          {
            "name": "玉溪",
            "code": "CN101290701",
            "name_en": "yuxi"
          },
          {
            "name": "澄江",
            "code": "CN101290702",
            "name_en": "chengjiang"
          },
          {
            "name": "江川",
            "code": "CN101290703",
            "name_en": "jiangchuan"
          },
          {
            "name": "通海",
            "code": "CN101290704",
            "name_en": "tonghai"
          },
          {
            "name": "华宁",
            "code": "CN101290705",
            "name_en": "huaning"
          },
          {
            "name": "新平",
            "code": "CN101290706",
            "name_en": "xinping"
          },
          {
            "name": "易门",
            "code": "CN101290707",
            "name_en": "yimen"
          },
          {
            "name": "峨山",
            "code": "CN101290708",
            "name_en": "eshan"
          },
          {
            "name": "元江",
            "code": "CN101290709",
            "name_en": "yuanjiang"
          }
        ]
      },
      {
        "name": "楚雄",
        "county": [
          {
            "name": "楚雄",
            "code": "CN101290801",
            "name_en": "chuxiong"
          },
          {
            "name": "大姚",
            "code": "CN101290802",
            "name_en": "dayao"
          },
          {
            "name": "元谋",
            "code": "CN101290803",
            "name_en": "yuanmou"
          },
          {
            "name": "姚安",
            "code": "CN101290804",
            "name_en": "yaoan"
          },
          {
            "name": "牟定",
            "code": "CN101290805",
            "name_en": "mouding"
          },
          {
            "name": "南华",
            "code": "CN101290806",
            "name_en": "nanhua"
          },
          {
            "name": "武定",
            "code": "CN101290807",
            "name_en": "wuding"
          },
          {
            "name": "禄丰",
            "code": "CN101290808",
            "name_en": "lufeng"
          },
          {
            "name": "双柏",
            "code": "CN101290809",
            "name_en": "shuangbai"
          },
          {
            "name": "永仁",
            "code": "CN101290810",
            "name_en": "yongren"
          }
        ]
      },
      {
        "name": "普洱",
        "county": [
          {
            "name": "普洱",
            "code": "CN101290901",
            "name_en": "puer"
          },
          {
            "name": "景谷",
            "code": "CN101290902",
            "name_en": "jinggu"
          },
          {
            "name": "景东",
            "code": "CN101290903",
            "name_en": "jingdong"
          },
          {
            "name": "澜沧",
            "code": "CN101290904",
            "name_en": "lancang"
          },
          {
            "name": "墨江",
            "code": "CN101290906",
            "name_en": "mojiang"
          },
          {
            "name": "江城",
            "code": "CN101290907",
            "name_en": "jiangcheng"
          },
          {
            "name": "孟连",
            "code": "CN101290908",
            "name_en": "menglian"
          },
          {
            "name": "西盟",
            "code": "CN101290909",
            "name_en": "ximeng"
          },
          {
            "name": "镇沅",
            "code": "CN101290911",
            "name_en": "zhenyuan"
          },
          {
            "name": "宁洱",
            "code": "CN101290912",
            "name_en": "ninger"
          }
        ]
      },
      {
        "name": "昭通",
        "county": [
          {
            "name": "昭通",
            "code": "CN101291001",
            "name_en": "zhaotong"
          },
          {
            "name": "鲁甸",
            "code": "CN101291002",
            "name_en": "ludian"
          },
          {
            "name": "彝良",
            "code": "CN101291003",
            "name_en": "yiliang"
          },
          {
            "name": "镇雄",
            "code": "CN101291004",
            "name_en": "zhenxiong"
          },
          {
            "name": "威信",
            "code": "CN101291005",
            "name_en": "weixin"
          },
          {
            "name": "巧家",
            "code": "CN101291006",
            "name_en": "qiaojia"
          },
          {
            "name": "绥江",
            "code": "CN101291007",
            "name_en": "suijiang"
          },
          {
            "name": "永善",
            "code": "CN101291008",
            "name_en": "yongshan"
          },
          {
            "name": "盐津",
            "code": "CN101291009",
            "name_en": "yanjin"
          },
          {
            "name": "大关",
            "code": "CN101291010",
            "name_en": "daguan"
          },
          {
            "name": "水富",
            "code": "CN101291011",
            "name_en": "shuifu"
          }
        ]
      },
      {
        "name": "临沧",
        "county": [
          {
            "name": "临沧",
            "code": "CN101291101",
            "name_en": "lincang"
          },
          {
            "name": "沧源",
            "code": "CN101291102",
            "name_en": "cangyuan"
          },
          {
            "name": "耿马",
            "code": "CN101291103",
            "name_en": "gengma"
          },
          {
            "name": "双江",
            "code": "CN101291104",
            "name_en": "shuangjiang"
          },
          {
            "name": "凤庆",
            "code": "CN101291105",
            "name_en": "fengqing"
          },
          {
            "name": "永德",
            "code": "CN101291106",
            "name_en": "yongde"
          },
          {
            "name": "云县",
            "code": "CN101291107",
            "name_en": "yunxian"
          },
          {
            "name": "镇康",
            "code": "CN101291108",
            "name_en": "zhenkang"
          }
        ]
      },
      {
        "name": "怒江",
        "county": [
          {
            "name": "怒江",
            "code": "CN101291201",
            "name_en": "nujiang"
          },
          {
            "name": "福贡",
            "code": "CN101291203",
            "name_en": "fugong"
          },
          {
            "name": "兰坪",
            "code": "CN101291204",
            "name_en": "lanping"
          },
          {
            "name": "泸水",
            "code": "CN101291205",
            "name_en": "lushui"
          },
          {
            "name": "六库",
            "code": "CN101291206",
            "name_en": "liuku"
          },
          {
            "name": "贡山",
            "code": "CN101291207",
            "name_en": "gongshan"
          }
        ]
      },
      {
        "name": "迪庆",
        "county": [
          {
            "name": "香格里拉",
            "code": "CN101291301",
            "name_en": "xianggelila"
          },
          {
            "name": "德钦",
            "code": "CN101291302",
            "name_en": "deqin"
          },
          {
            "name": "维西",
            "code": "CN101291303",
            "name_en": "weixi"
          },
          {
            "name": "中甸",
            "code": "CN101291304",
            "name_en": "zhongdian"
          }
        ]
      },
      {
        "name": "丽江",
        "county": [
          {
            "name": "丽江",
            "code": "CN101291401",
            "name_en": "lijiang"
          },
          {
            "name": "永胜",
            "code": "CN101291402",
            "name_en": "yongsheng"
          },
          {
            "name": "华坪",
            "code": "CN101291403",
            "name_en": "huaping"
          },
          {
            "name": "宁蒗",
            "code": "CN101291404",
            "name_en": "ninglang"
          }
        ]
      },
      {
        "name": "德宏",
        "county": [
          {
            "name": "德宏",
            "code": "CN101291501",
            "name_en": "dehong"
          },
          {
            "name": "陇川",
            "code": "CN101291503",
            "name_en": "longchuan"
          },
          {
            "name": "盈江",
            "code": "CN101291504",
            "name_en": "yingjiang"
          },
          {
            "name": "瑞丽",
            "code": "CN101291506",
            "name_en": "ruili"
          },
          {
            "name": "梁河",
            "code": "CN101291507",
            "name_en": "lianghe"
          },
          {
            "name": "芒市",
            "code": "CN101291508",
            "name_en": "luxi"
          }
        ]
      },
      {
        "name": "西双版纳",
        "county": [
          {
            "name": "景洪",
            "code": "CN101291601",
            "name_en": "jinghong"
          },
          {
            "name": "勐海",
            "code": "CN101291603",
            "name_en": "menghai"
          },
          {
            "name": "勐腊",
            "code": "CN101291605",
            "name_en": "mengla"
          }
        ]
      }
    ]
  },
  {
    "name": "广西",
    "name_en": "guangxi",
    "city": [
      {
        "name": "南宁",
        "county": [
          {
            "name": "南宁",
            "code": "CN101300101",
            "name_en": "nanning"
          },
          {
            "name": "邕宁",
            "code": "CN101300103",
            "name_en": "yongning"
          },
          {
            "name": "横县",
            "code": "CN101300104",
            "name_en": "hengxian"
          },
          {
            "name": "隆安",
            "code": "CN101300105",
            "name_en": "longan"
          },
          {
            "name": "马山",
            "code": "CN101300106",
            "name_en": "mashan"
          },
          {
            "name": "上林",
            "code": "CN101300107",
            "name_en": "shanglin"
          },
          {
            "name": "武鸣",
            "code": "CN101300108",
            "name_en": "wuming"
          },
          {
            "name": "宾阳",
            "code": "CN101300109",
            "name_en": "binyang"
          }
        ]
      },
      {
        "name": "崇左",
        "county": [
          {
            "name": "崇左",
            "code": "CN101300201",
            "name_en": "chongzuo"
          },
          {
            "name": "天等",
            "code": "CN101300202",
            "name_en": "tiandeng"
          },
          {
            "name": "龙州",
            "code": "CN101300203",
            "name_en": "longzhou"
          },
          {
            "name": "凭祥",
            "code": "CN101300204",
            "name_en": "pingxiang"
          },
          {
            "name": "大新",
            "code": "CN101300205",
            "name_en": "daxin"
          },
          {
            "name": "扶绥",
            "code": "CN101300206",
            "name_en": "fusui"
          },
          {
            "name": "宁明",
            "code": "CN101300207",
            "name_en": "ningming"
          }
        ]
      },
      {
        "name": "柳州",
        "county": [
          {
            "name": "柳州",
            "code": "CN101300301",
            "name_en": "liuzhou"
          },
          {
            "name": "柳城",
            "code": "CN101300302",
            "name_en": "liucheng"
          },
          {
            "name": "鹿寨",
            "code": "CN101300304",
            "name_en": "luzhai"
          },
          {
            "name": "柳江",
            "code": "CN101300305",
            "name_en": "liujiang"
          },
          {
            "name": "融安",
            "code": "CN101300306",
            "name_en": "rongan"
          },
          {
            "name": "融水",
            "code": "CN101300307",
            "name_en": "rongshui"
          },
          {
            "name": "三江",
            "code": "CN101300308",
            "name_en": "sanjiang"
          }
        ]
      },
      {
        "name": "来宾",
        "county": [
          {
            "name": "来宾",
            "code": "CN101300401",
            "name_en": "laibin"
          },
          {
            "name": "忻城",
            "code": "CN101300402",
            "name_en": "xicheng"
          },
          {
            "name": "金秀",
            "code": "CN101300403",
            "name_en": "jinxiu"
          },
          {
            "name": "象州",
            "code": "CN101300404",
            "name_en": "xiangzhou"
          },
          {
            "name": "武宣",
            "code": "CN101300405",
            "name_en": "wuxuan"
          },
          {
            "name": "合山",
            "code": "CN101300406",
            "name_en": "heshan"
          }
        ]
      },
      {
        "name": "桂林",
        "county": [
          {
            "name": "桂林",
            "code": "CN101300501",
            "name_en": "guilin"
          },
          {
            "name": "龙胜",
            "code": "CN101300503",
            "name_en": "longsheng"
          },
          {
            "name": "永福",
            "code": "CN101300504",
            "name_en": "yongfu"
          },
          {
            "name": "临桂",
            "code": "CN101300505",
            "name_en": "lingui"
          },
          {
            "name": "兴安",
            "code": "CN101300506",
            "name_en": "xingan"
          },
          {
            "name": "灵川",
            "code": "CN101300507",
            "name_en": "lingchuan"
          },
          {
            "name": "全州",
            "code": "CN101300508",
            "name_en": "quanzhou"
          },
          {
            "name": "灌阳",
            "code": "CN101300509",
            "name_en": "guanyang"
          },
          {
            "name": "阳朔",
            "code": "CN101300510",
            "name_en": "yangshuo"
          },
          {
            "name": "恭城",
            "code": "CN101300511",
            "name_en": "gongcheng"
          },
          {
            "name": "平乐",
            "code": "CN101300512",
            "name_en": "pingle"
          },
          {
            "name": "荔浦",
            "code": "CN101300513",
            "name_en": "lipu"
          },
          {
            "name": "资源",
            "code": "CN101300514",
            "name_en": "ziyuan"
          }
        ]
      },
      {
        "name": "梧州",
        "county": [
          {
            "name": "梧州",
            "code": "CN101300601",
            "name_en": "wuzhou"
          },
          {
            "name": "藤县",
            "code": "CN101300602",
            "name_en": "tengxian"
          },
          {
            "name": "苍梧",
            "code": "CN101300604",
            "name_en": "cangwu"
          },
          {
            "name": "蒙山",
            "code": "CN101300605",
            "name_en": "mengshan"
          },
          {
            "name": "岑溪",
            "code": "CN101300606",
            "name_en": "cenxi"
          }
        ]
      },
      {
        "name": "贺州",
        "county": [
          {
            "name": "贺州",
            "code": "CN101300701",
            "name_en": "hezhou"
          },
          {
            "name": "昭平",
            "code": "CN101300702",
            "name_en": "zhaoping"
          },
          {
            "name": "富川",
            "code": "CN101300703",
            "name_en": "fuchuan"
          },
          {
            "name": "钟山",
            "code": "CN101300704",
            "name_en": "zhongshan"
          }
        ]
      },
      {
        "name": "贵港",
        "county": [
          {
            "name": "贵港",
            "code": "CN101300801",
            "name_en": "guigang"
          },
          {
            "name": "桂平",
            "code": "CN101300802",
            "name_en": "guiping"
          },
          {
            "name": "平南",
            "code": "CN101300803",
            "name_en": "pingnan"
          }
        ]
      },
      {
        "name": "玉林",
        "county": [
          {
            "name": "玉林",
            "code": "CN101300901",
            "name_en": "yulin"
          },
          {
            "name": "博白",
            "code": "CN101300902",
            "name_en": "bobai"
          },
          {
            "name": "北流",
            "code": "CN101300903",
            "name_en": "beiliu"
          },
          {
            "name": "容县",
            "code": "CN101300904",
            "name_en": "rongxian"
          },
          {
            "name": "陆川",
            "code": "CN101300905",
            "name_en": "luchuan"
          },
          {
            "name": "兴业",
            "code": "CN101300906",
            "name_en": "xingye"
          }
        ]
      },
      {
        "name": "百色",
        "county": [
          {
            "name": "百色",
            "code": "CN101301001",
            "name_en": "baise"
          },
          {
            "name": "那坡",
            "code": "CN101301002",
            "name_en": "napo"
          },
          {
            "name": "田阳",
            "code": "CN101301003",
            "name_en": "tianyang"
          },
          {
            "name": "德保",
            "code": "CN101301004",
            "name_en": "debao"
          },
          {
            "name": "靖西",
            "code": "CN101301005",
            "name_en": "jingxi"
          },
          {
            "name": "田东",
            "code": "CN101301006",
            "name_en": "tiandong"
          },
          {
            "name": "平果",
            "code": "CN101301007",
            "name_en": "pingguo"
          },
          {
            "name": "隆林",
            "code": "CN101301008",
            "name_en": "longlin"
          },
          {
            "name": "西林",
            "code": "CN101301009",
            "name_en": "xilin"
          },
          {
            "name": "乐业",
            "code": "CN101301010",
            "name_en": "leye"
          },
          {
            "name": "凌云",
            "code": "CN101301011",
            "name_en": "lingyun"
          },
          {
            "name": "田林",
            "code": "CN101301012",
            "name_en": "tianlin"
          }
        ]
      },
      {
        "name": "钦州",
        "county": [
          {
            "name": "钦州",
            "code": "CN101301101",
            "name_en": "qinzhou"
          },
          {
            "name": "浦北",
            "code": "CN101301102",
            "name_en": "pubei"
          },
          {
            "name": "灵山",
            "code": "CN101301103",
            "name_en": "lingshan"
          }
        ]
      },
      {
        "name": "河池",
        "county": [
          {
            "name": "河池",
            "code": "CN101301201",
            "name_en": "hechi"
          },
          {
            "name": "天峨",
            "code": "CN101301202",
            "name_en": "tiane"
          },
          {
            "name": "东兰",
            "code": "CN101301203",
            "name_en": "donglan"
          },
          {
            "name": "巴马",
            "code": "CN101301204",
            "name_en": "bama"
          },
          {
            "name": "环江",
            "code": "CN101301205",
            "name_en": "huanjiang"
          },
          {
            "name": "罗城",
            "code": "CN101301206",
            "name_en": "luocheng"
          },
          {
            "name": "宜州",
            "code": "CN101301207",
            "name_en": "yizhou"
          },
          {
            "name": "凤山",
            "code": "CN101301208",
            "name_en": "fengshan"
          },
          {
            "name": "南丹",
            "code": "CN101301209",
            "name_en": "nandan"
          },
          {
            "name": "都安",
            "code": "CN101301210",
            "name_en": "andu"
          },
          {
            "name": "大化",
            "code": "CN101301211",
            "name_en": "dahua"
          }
        ]
      },
      {
        "name": "北海",
        "county": [
          {
            "name": "北海",
            "code": "CN101301301",
            "name_en": "beihai"
          },
          {
            "name": "合浦",
            "code": "CN101301302",
            "name_en": "hepu"
          },
          {
            "name": "涠洲岛",
            "code": "CN101301303",
            "name_en": "weizhoudao"
          }
        ]
      },
      {
        "name": "防城港",
        "county": [
          {
            "name": "防城港",
            "code": "CN101301401",
            "name_en": "fangchenggang"
          },
          {
            "name": "上思",
            "code": "CN101301402",
            "name_en": "shangsi"
          },
          {
            "name": "东兴",
            "code": "CN101301403",
            "name_en": "dongxing"
          },
          {
            "name": "防城",
            "code": "CN101301405",
            "name_en": "fangcheng"
          }
        ]
      }
    ]
  },
  {
    "name": "海南",
    "name_en": "hainan",
    "city": [
      {
        "name": "海口",
        "county": [
          {
            "name": "海口",
            "code": "CN101310101",
            "name_en": "haikou"
          }
        ]
      },
      {
        "name": "三亚",
        "county": [
          {
            "name": "三亚",
            "code": "CN101310201",
            "name_en": "sanya"
          }
        ]
      },
      {
        "name": "东方",
        "county": [
          {
            "name": "东方",
            "code": "CN101310202",
            "name_en": "dongfang"
          }
        ]
      },
      {
        "name": "临高",
        "county": [
          {
            "name": "临高",
            "code": "CN101310203",
            "name_en": "lingao"
          }
        ]
      },
      {
        "name": "澄迈",
        "county": [
          {
            "name": "澄迈",
            "code": "CN101310204",
            "name_en": "chengmai"
          }
        ]
      },
      {
        "name": "儋州",
        "county": [
          {
            "name": "儋州",
            "code": "CN101310205",
            "name_en": "danzhou"
          }
        ]
      },
      {
        "name": "昌江",
        "county": [
          {
            "name": "昌江",
            "code": "CN101310206",
            "name_en": "changjiang"
          }
        ]
      },
      {
        "name": "白沙",
        "county": [
          {
            "name": "白沙",
            "code": "CN101310207",
            "name_en": "baisha"
          }
        ]
      },
      {
        "name": "琼中",
        "county": [
          {
            "name": "琼中",
            "code": "CN101310208",
            "name_en": "qiongzhong"
          }
        ]
      },
      {
        "name": "定安",
        "county": [
          {
            "name": "定安",
            "code": "CN101310209",
            "name_en": "dingan"
          }
        ]
      },
      {
        "name": "屯昌",
        "county": [
          {
            "name": "屯昌",
            "code": "CN101310210",
            "name_en": "tunchang"
          }
        ]
      },
      {
        "name": "琼海",
        "county": [
          {
            "name": "琼海",
            "code": "CN101310211",
            "name_en": "qionghai"
          }
        ]
      },
      {
        "name": "文昌",
        "county": [
          {
            "name": "文昌",
            "code": "CN101310212",
            "name_en": "wenchang"
          }
        ]
      },
      {
        "name": "保亭",
        "county": [
          {
            "name": "保亭",
            "code": "CN101310214",
            "name_en": "baoting"
          }
        ]
      },
      {
        "name": "万宁",
        "county": [
          {
            "name": "万宁",
            "code": "CN101310215",
            "name_en": "wanning"
          }
        ]
      },
      {
        "name": "陵水",
        "county": [
          {
            "name": "陵水",
            "code": "CN101310216",
            "name_en": "lingshui"
          }
        ]
      },
      {
        "name": "西沙",
        "county": [
          {
            "name": "西沙",
            "code": "CN101310217",
            "name_en": "xisha"
          }
        ]
      },
      {
        "name": "南沙",
        "county": [
          {
            "name": "南沙",
            "code": "CN101310220",
            "name_en": "nansha"
          }
        ]
      },
      {
        "name": "乐东",
        "county": [
          {
            "name": "乐东",
            "code": "CN101310221",
            "name_en": "ledong"
          }
        ]
      },
      {
        "name": "五指山",
        "county": [
          {
            "name": "五指山",
            "code": "CN101310222",
            "name_en": "wuzhishan"
          }
        ]
      },
      {
        "name": "中沙",
        "county": [
          {
            "name": "中沙",
            "code": "CN101310224",
            "name_en": "zhongsha"
          }
        ]
      },
      {
        "name": "南子岛",
        "county": [
          {
            "name": "南子岛",
            "code": "CN101310230",
            "name_en": "nanzidao"
          }
        ]
      }
    ]
  },
  {
    "name": "香港",
    "name_en": "xianggang",
    "city": [
      {
        "name": "香港",
        "county": [
          {
            "name": "香港",
            "code": "CN101320101",
            "name_en": "hongkong"
          },
          {
            "name": "九龙",
            "code": "CN101320102",
            "name_en": "jiulong"
          },
          {
            "name": "新界",
            "code": "CN101320103",
            "name_en": "xinjie"
          }
        ]
      }
    ]
  },
  {
    "name": "澳门",
    "name_en": "aomen",
    "city": [
      {
        "name": "澳门",
        "county": [
          {
            "name": "澳门",
            "code": "CN101330101",
            "name_en": "macao"
          },
          {
            "name": "氹仔岛",
            "code": "CN101330102",
            "name_en": "dangzidao"
          },
          {
            "name": "路环岛",
            "code": "CN101330103",
            "name_en": "luhuandao"
          }
        ]
      }
    ]
  },
  {
    "name": "台湾",
    "name_en": "taiwan",
    "city": [
      {
        "name": "台北",
        "county": [
          {
            "name": "台北",
            "code": "CN101340101",
            "name_en": "taibeixian"
          },
          {
            "name": "桃园",
            "code": "CN101340102",
            "name_en": "taoyuan"
          },
          {
            "name": "新竹",
            "code": "CN101340103",
            "name_en": "xinzhu"
          },
          {
            "name": "宜兰",
            "code": "CN101340104",
            "name_en": "yilan"
          }
        ]
      },
      {
        "name": "高雄",
        "county": [
          {
            "name": "高雄",
            "code": "CN101340201",
            "name_en": "gaoxiong"
          },
          {
            "name": "嘉义",
            "code": "CN101340202",
            "name_en": "jiayi"
          },
          {
            "name": "台南",
            "code": "CN101340203",
            "name_en": "tainan"
          },
          {
            "name": "台东",
            "code": "CN101340204",
            "name_en": "taidong"
          },
          {
            "name": "屏东",
            "code": "CN101340205",
            "name_en": "pingdong"
          }
        ]
      },
      {
        "name": "台中",
        "county": [
          {
            "name": "台中",
            "code": "CN101340401",
            "name_en": "taizhong"
          },
          {
            "name": "苗栗",
            "code": "CN101340402",
            "name_en": "miaoli"
          },
          {
            "name": "彰化",
            "code": "CN101340403",
            "name_en": "zhanghua"
          },
          {
            "name": "南投",
            "code": "CN101340404",
            "name_en": "nantou"
          },
          {
            "name": "花莲",
            "code": "CN101340405",
            "name_en": "hualian"
          },
          {
            "name": "云林",
            "code": "CN101340406",
            "name_en": "yunlin"
          }
        ]
      }
    ]
  }
]
  city_ls=[]
  for i in range(x):
    #省
    n=randint(0,33)
    #市
    m=randint(0,citys[n]['city'].__len__()-1)
    #区
    p=randint(0,citys[n]['city'][m]['county'].__len__()-1)
    # print(citys[n]['name'],citys[n]['city'][m]['name'],citys[n]['city'][m]['county'][p]['name'])
  # print(citys[3]['name'], citys[3]['city'][0]['name'], citys[3]['city'][0]['county'][2]['name'])
    city_ls.append([citys[n]['name'],citys[n]['city'][m]['name'],citys[n]['city'][m]['county'][p]['name']])
  return city_ls

city(5)


