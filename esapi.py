# -*- coding:utf-8 -*-
import json

__author__ = 'zhennehz'

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

class ElasticObj:
    def __init__(self, index_name,index_type,ip ="127.0.0.1"):
        '''

        :param index_name: 索引名称
        :param index_type: 索引类型
        '''
        self.index_name =index_name
        self.index_type = index_type
        # 无用户名密码状态
        #self.es = Elasticsearch([ip])
        #用户名密码状态
        self.es = Elasticsearch([ip],http_auth=('elastic', 'password'),port=9200)

    def create_index(self,index_name="ott2",index_type="doc"):
        '''
        创建索引,创建索引名称为ott，类型为doc的索引
        :param ex: Elasticsearch对象
        :return:
        '''
        #创建映射
        _index_mappings = {
            "mappings": {
                self.index_type: {
                  "properties": {
                    "Region": {
                      "type": "keyword"
                    },
                    "Country": {
                      "type": "keyword"
                    },
                    "State": {
                      "type": "keyword"
                    },
                    "City": {
                      "type": "keyword"
                    },
                    "Month": {
                      "type": "integer"
                    },
                    "Day": {
                      "type": "integer"
                    },
                    "Year": {
                      "type": "integer"
                    },
                    "AvgTemperature": {
                      "type": "float"
                    }
                  }
                }

            }
        }
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index=self.index_name, body=_index_mappings)
            print(res)




    def Index_Data(self):
        '''
        数据存储到es
        :return:
        '''
        list = [
            {
                "DOCNO": "AP890301-0058",
                "FILEID": "AP-NR-03-01-89 0556EST",
                "FIRST": "r w PM-WrightProbe 1stLd-Writethru a0512 03-01 0334",
                "SECOND": "PM-Wright Probe, 1st Ld-Writethru, a0512,300",
                "HEAD": [
                    "Speaker Reportedly Threatened to Expose Official's Homosexuality",
                    "Eds: LEADS with 3 grafs to make it thrift official sted banking official;picks up 4th graf pvs, bgng: ``Executives of...''"
                ],
                "DATELINE": "WASHINGTON (AP)",
                "TEXT": "The ethics investigation of House Speaker JimWright was expanded to include an allegation that he threatened toexpose a federal thrift regulator's homosexuality unless Texasthrift executives gained access to Washington officials, TheWashington Times reported today.Wright said through a spokesman the allegation was``preposterous,'' the newspaper said.The Times quoted sources as saying Wright was accused ofthreatening federal officials in Washington with ``blowing thewhistle'' on a federal thrift regulator's alleged homosexualityunless Texas thrift executives were allowed to meet with Washingtonofficials of the Federal Home Loan Bank Board.Executives of at least two Texas savings and loan associationsfelt they could not get fair hearings at the bank board's Dallasoffice, where the federal official in question worked, the Timessaid. The Texas thrift executives were complaining ofover-regulation, and some of them were friends of the speaker, thenewspaper said.Wright's spokesman, Mark Johnson, told the newspaper, ``Thespeaker never threatened to expose anything. It's a figment ofsomeone's imagination, someone with an obvious ax to grind.''Wright has been investigated by the House Committee on Standardsof Official Conduct since last fall regarding alleged attempts toinfluence federal regulators on behalf of several Texas savings andloan executives. He also has been accused of accepting a Fort Worthcondominium at a price below market value, of ordering a member ofhis staff to work on his book and of using the book's royalties toskirt limits on outside income.Wright has denied any wrongdoing. A report was submitted to theHouse ethics panel last week by its counsel, and the panel mustdecide whether it believes any of the charges were substantiated.The Times said the new allegation was brought to the committee'sattention in December or January."
            },
            {
                "DOCNO": "AP890301-0059",
                "FILEID": "AP-NR-03-01-89 0559EST",
                "FIRST": "r a PM-BlindTV     03-01 0541",
                "SECOND": "PM-Blind TV,0554",
                "HEAD": "Public TV Station Plans Service To Make Television Vivid For TheBlind",
                "BYLINE": [
                    "By ARLENE LEVINSON",
                    "Associated Press Writer"
                ],
                "DATELINE": "BOSTON (AP)",
                "TEXT": "A public television station has developed a servicethat makes TV vivid for the blind and visually impaired by having anarrator describe a program's setting and action during pauses indialogue.The service, developed by Boston's WGBH-TV, which also pioneeredclosed captions for the hearing impaired 15 years ago, broadcaststhe added narration over a special channel that can be tapped bypeople with a stereo television or a video cassette recorder.The station tested the service last year and is seeking fundingto make it available in January 1990 to the nation's estimated 12million visually impaired people.``I never realized when I watched television, from a listeningperspective, that I was missing so much,'' Kim Charlson recalledTuesday. Blind since the age of 11, the 31-year-old Watertownresident was among thousands of visually impaired people across thecountry who tuned to the service's trial run.Television ``is a major means of communication in society,'' Mrs.Charlson said. ``There's so much on television, you tend to feelleft out when you can't access it. I really commend them thatthey're trying to do it, and do it right.''Descriptive Video Services allows anyone with visual impairment _or even sighted people stepping away from their TV set _ to followthe show. With a stereo television set or VCR tuned to the SeparateAudio Program channel, they can hear a narrator describe a program'sscene and action during musical interludes or breaks in dialogue.WGBH enlisted nine other public TV stations to test the servicefrom January to July 1988 on the PBS ``American Playhouse'' dramaseries.A viewer tuned to the play ``Lemon Sky,'' for example, could hearas the credits rolled: ``A mountain silhouette in the distance, palmtrees closer. A boy's bike between a high, brown wooden fence. Inthe foreground a white, mid-'50s convertible gleaming in the sun,its top down.''Then later, after a character spoke his lines: ``He strolls awayfrom the car toward the house, pausing in the doorway.''``I see it as something that can become widely popular and shouldbe,'' said John De Witt, who evaluates high-tech aides for the blindat the American Federation for the Blind in New York.``It's not a question only of people who are totally blind,'' DeWitt said in a telephone interview. ``There are millions of peoplewho have very poor vision and cannot see small details on thescreen, people who are losing their vision at any time of life.''The establishment of the Separate Audio Program channel aboutfive years ago makes the new television service possible. About 10percent of American homes can tap the audio channel now, and LaurieEverett, director of Descriptive Video Services, predicted access tothe channel would be common by the turn of the century.``In a couple of years you won't be able to buy a television thatisn't stereo,'' she said.WGBH is trying to raise $300,000 to launch the service nationallyfive hours a week and needs $1 million annually to keep it going,Ms. Everett said."
            }

        ]
        for item in list:
            res = self.es.index(index=self.index_name, doc_type=self.index_type, body=item)
            print(res)

    def bulk_Index_Data(self,list):
        '''
        用bulk将批量数据存储到es
        :return:
        '''
        ACTIONS = []
        i = 1
        for line in list:
            action = {
                "_index": self.index_name,
                "_type": self.index_type,
                "_source": line
            }
            i += 1
            ACTIONS.append(action)
            # 批量处理
        success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)
        print('Performed %d actions' % success)

    def Delete_Index_Data(self,id):
        '''
        删除索引中的一条
        :param id:
        :return:
        '''
        res = self.es.delete(index=self.index_name, doc_type=self.index_type, id=id)
        print (res)

    def Get_Data_Id(self,id):

        res = self.es.get(index=self.index_name, doc_type=self.index_type,id=id)
        print(res['_source'])

        print ('------------------------------------------------------------------')
        #
        # # 输出查询到的结果
        for hit in res['hits']['hits']:
            print (hit['_source'])

    def Get_Data_By_Body(self,queryStr):
        if queryStr is None or len(queryStr)==0:
            queryStr = {'match_all': {}}
        doc = {
            "query": queryStr,
            "from": 0,
            "size": 50
        }
        # doc = {'query': {'match_all': {}}}
        # doc = {
        #       "query": {
        #         "bool": {
        #           "must": [
        #             {
        #               "match": {
        #                 "Region": word
        #               }
        #             },
        #               {
        #                   "match": {
        #                       "City": "Lusaka"
        #                   }
        #               },
        #               {
        #                   "range": {
        #                       "Day": {
        #                         "gte": 11,
        #                         "lte": 13
        #                       }
        #                   }
        #               }
        #           ]
        #         }
        #       },
        #       "from": 0,
        #       "size": 50
        # }
        print(doc)
        _searched = self.es.search(index=self.index_name, doc_type=self.index_type, body=doc)

        list = []
        for hit in _searched['hits']['hits']:
            list.append(hit['_source'])
            print (hit['_source'])

        return list




esobj =ElasticObj("ott2","doc",ip ="127.0.0.1")
# esobj = ElasticObj("ott2", "doc")

esobj.create_index(index_name="ott2")
# esobj.Index_Data()
# esobj.bulk_Index_Data()
# esobj.Delete_Index_Data(1)
# list = esobj.Get_Data_By_Body('')
# # print(list)