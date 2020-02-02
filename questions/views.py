from django.shortcuts import render
from .models import *
import json
from rest_framework.response import Response
from django.forms.models import model_to_dict
from random import randint
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import UserTestSerializer
# Create your views here.
class get_question(APIView):
     permission_classes=(IsAuthenticated,)
     def get(self,request):
          the_user=request.user
          if the_user :
               pervious_questions=UserTest.objects.filter(user=the_user)

               lis_prev_test=[]
               for pq in pervious_questions:
                    lis_prev_test.append(model_to_dict(pq)["tst"])
               retList=[]
               count = len(lis_prev_test)
               if count<16:
                    for i in range(5):
                         random_index = randint(0, 19-count )
                         temp_question=Test.objects.exclude(id__in=lis_prev_test)[random_index]
                         lis_prev_test.append(temp_question.id)
                         count = len(lis_prev_test)
                         ut=UserTest(tst=temp_question,user=the_user,q_numer=count)
                         temp_dic={
                              "question #":count,
                              "text": temp_question.text,
                              "01":  temp_question.Asn1,
                              "02":  temp_question.Asn2,
                              "03":  temp_question.Asn3,
                              "04":  temp_question.Asn4
                         }
                         retList.append(temp_dic)

                         ut.save()

                    return Response({"resp":retList})
               else:
                    return Response({"status":"your test End  "})
          else:
               return Response({"status":"you dont register"})


class get_all_question(APIView):
     def get(self,request):
          the_user=request.user
          if the_user:
               pervious_questions=UserTest.objects.filter(user=the_user)
               lis_prev_test=[]
               for pq in pervious_questions:
                    serial=UserTestSerializer(pq)
                    lis_prev_test.append(serial.data)
               return Response({"res":lis_prev_test})     
          else:
               return Response({"status":"you dont register yet"})

class get_single_question(APIView):
     def post(self,request):
          pass
    


#      def answer(request):
#           body_unicode=request.body.decode('utf-8')
#           body=json.loads(body_unicode)
#           user_name=body["name"]
#           the_user=user.objects.filter(name=user_name).first()
#           if user_name:
#                pervious_questions=user_test.objects.filter(user=the_user)
#                lis_prev_test=[]
#                for pq in pervious_questions:
#                     ans=test.objects.filter(id=model_to_dict(pq)["test"]).first()
#                     ans=model_to_dict(ans)["TrueAns"]
#                     lis_prev_test.append({
#                     "soalId":model_to_dict(pq)["test"],
#                     "soalU":model_to_dict(pq)["q_numer"],
#                     "ans":ans
#                     })

#                ghalat=0
#                dorost=0
#                # return JsonResponse({"res":lis_prev_test})

#                s1=body["s1"]
#                jvb1=body["jvb1"]

#                s2=body["s2"]
#                jvb2=body["jvb2"]

#                s3=body["s3"]
#                jvb3=body["jvb3"]

#                s4=body["s4"]
#                jvb4=body["jvb4"]

#                s5=body["s5"]
#                jvb5=body["jvb5"]
#                for t in lis_prev_test:
#                     if s1==t["soalU"]:
#                          if jvb1==t["ans"]:
#                               dorost +=1
#                          elif not jvb1:
#                               pass
#                          else:
#                               ghalat +=1     

#                     if s2==t["soalU"]:
#                          if jvb2==t["ans"]:
#                               dorost +=1
#                          elif not jvb1:
#                               pass
#                          else:
#                               ghalat +=1         

#                     if s3==t["soalU"]:
#                          if jvb3==t["ans"]:
#                               dorost +=1
#                          elif not jvb3:
#                               pass
#                          else:
#                               ghalat +=1     

#                     if s4==t["soalU"]:
#                          if jvb4==t["ans"]:
#                               dorost +=1
#                          elif not jvb4:
#                               pass
#                          else:
#                               ghalat +=1     
#                     if s5==t["soalU"]:
#                          if jvb5==t["ans"]:
#                               dorost +=1
#                          elif not jvb5:
#                               pass
#                          else:
#                               ghalat +=1     
#                percent=((dorost*3-ghalat)/15)*100               
#                return JsonResponse({"percent":percent})
     
#           else:
#                return JsonResponse({"status":"you dont register"})

# def get_all_question(request):
#      alll=test.objects.all()
#      ans=[]
#      for t in alll:
#           ans.append(model_to_dict(t))
#      return JsonResponse({"resp":ans})


def addAlltoDb(request):
     resp=[]
     pass
     # with open("q.txt",'r')as file:
     #    tempasn={}
     #    i=1
     #    tempsoal=""
     #    tempJvb1=""
     #    tempJvb2=""
     #    tempJvb3=""
     #    tempJvb4=""
     #    tempDorst=0
     #    for line in file:
     #        if line.startswith("#"):
     #            line=line[1:]
     #            tempDorst=i-1
     #            tempasn["javab"]=tempDorst
     #        if i==1:
     #            tempsoal=line
     #            tempasn["soal"]=line
     #            i+=1
     #        elif i==2:
     #            tempasn["j1"]=line
     #            tempJvb1=line
     #            i+=1
     #        elif i==3:
     #            tempasn["j2"]=line
     #            tempJvb2=line

     #            i+=1
     #        elif i==4:
     #            tempasn["j3"]=line
     #            tempJvb3=line
     #            i+=1
     #        elif  i==5:
     #            tempasn["j4"]=line
     #            tempJvb4=line
     #            i=1
     #            resp.append(tempasn)
     #            t=Test(text=tempsoal,Asn1=tempJvb1,Asn2=tempJvb2,Asn3=tempJvb3,Asn4=tempJvb4,TrueAns=tempDorst)
     #            t.save()
     #            tempsoal=""
     #            tempJvb1=""
     #            tempJvb2=""
     #            tempJvb3=""
     #            tempJvb4=""
     #            tempDorst=0

     #    return JsonResponse({"status":resp})
