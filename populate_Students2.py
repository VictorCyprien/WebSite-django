import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django.setup()

from lycee.models import *
# creation de cursus
c1=Cursus()
c1.name="BTS SIO"
c1.year_from_bac = 1
c1.scholar_year = '2018-2019'
c1.save()
#
c2=Cursus()
c2.name="BTS SN"
c2.year_from_bac = 1
c2.scholar_year = '2018-2019'
c2.save()
#
c3=Cursus()
c3.name="BTS DIET"
c3.year_from_bac = 1
c3.scholar_year = '2018-2019'
c3.save()
#
c4=Cursus()
c4.name="BTS COMPTA"
c4.year_from_bac = 1
c4.scholar_year = '2018-2019'
c4.save()
# recup des cles primaires
cp1= Cursus.objects.get(name__contains = "sio")
cp2= Cursus.objects.get(name__contains = "sn")
cp3= Cursus.objects.get(name__contains = "diet")
cp4= Cursus.objects.get(name__contains = "compta")

# creation d'etudiants
st1 = Student(
    last_name 	=  'SMITH',
    first_name 	= 'MARY',
    phone 		= '0123456789',
    email 		= 'MARY.SMITH@limayrac.fr',
    birth_date 		= datetime(1999,12,31),
    comments 	= "no comment",
    cursus      = cp1,
)
st1.save()
st1 = Student(
last_name 	= 'JOHNSON',
first_name 	= 'PATRICIA',
phone 		= '0123456790',
email 		= 'PATRICIA.JOHNSON@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp1,
)
st1.save()
st1 = Student(
last_name 	= 'WILLIAMS',
first_name 	= 'LINDA',
phone 		= '0123456791',
email 		= 'LINDA.WILLIAMS@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'JONES',
first_name 	= 'BARBARA',
phone 		= '0123456792',
email 		= 'BARBARA.JONES@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'BROWN',
first_name 	= 'ELIZABETH',
phone 		= '0123456793',
email 		= 'ELIZABETH.BROWN@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'DAVIS',
first_name 	= 'JENNIFER',
phone 		= '0123456794',
email 		= 'JENNIFER.DAVIS@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'MILLER',
first_name 	= 'MARIA',
phone 		= '0123456795',
email 		= 'MARIA.MILLER@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'WILSON',
first_name 	= 'SUSAN',
phone 		= '0123456796',
email 		= 'SUSAN.WILSON@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'MOORE',
first_name 	= 'MARGARET',
phone 		= '0123456797',
email 		= 'MARGARET.MOORE@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'TAYLOR',
first_name 	= 'Dorothee',
phone 		= '0123456798',
email 		= 'DOROTHY.TAYLOR@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'ANDERSON',
first_name 	= 'LISA',
phone 		= '0123456799',
email 		= 'LISA.ANDERSON@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'THOMAS',
first_name 	= 'NANCY',
phone 		= '0123456800',
email 		= 'NANCY.THOMAS@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'JACKSON',
first_name 	= 'KAREN',
phone 		= '0123456801',
email 		= 'KAREN.JACKSON@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'WHITE',
first_name 	= 'BETTY',
phone 		= '0123456802',
email 		= 'BETTY.WHITE@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'HARRIS',
first_name 	= 'HELEN',
phone 		= '0123456803',
email 		= 'HELEN.HARRIS@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'MARTIN',
first_name 	= 'SANDRA',
phone 		= '0123456804',
email 		= 'SANDRA.MARTIN@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'THOMPSON',
first_name 	= 'DONNA',
phone 		= '0123456805',
email 		= 'DONNA.THOMPSON@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'GARCIA',
first_name 	= 'CAROL',
phone 		= '0123456806',
email 		= 'CAROL.GARCIA@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'MARTINEZ',
first_name 	= 'RUTH',
phone 		= '0123456807',
email 		= 'RUTH.MARTINEZ@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'ROBINSON',
first_name 	= 'SHARON',
phone 		= '0123456808',
email 		= 'SHARON.ROBINSON@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'CLARK',
first_name 	= 'MICHELLE',
phone 		= '0123456809',
email 		= 'MICHELLE.CLARK@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'RODRIGUEZ',
first_name 	= 'LAURA',
phone 		= '0123456810',
email 		= 'LAURA.RODRIGUEZ@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'LEWIS',
first_name 	= 'SARAH',
phone 		= '0123456811',
email 		= 'SARAH.LEWIS@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'LEE',
first_name 	= 'KIMBERLY',
phone 		= '0123456812',
email 		= 'KIMBERLY.LEE@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st1 = Student(
last_name 	= 'WALKER',
first_name 	= 'DEBORAH',
phone 		= '0123456813',
email 		= 'DEBORAH.WALKER@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= 	 "no comment",
cursus      = cp1,)
st1.save()
st2 = Student(
last_name 	= 'HALL',
first_name 	= 'JESSICA',
phone 		= '0123456814',
email 		= 'JESSICA.HALL@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'ALLEN',
first_name 	= 'SHIRLEY',
phone 		= '0123456815',
email 		= 'SHIRLEY.ALLEN@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= 	 "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'YOUNG',
first_name 	= 'CYNTHIA',
phone 		= '0123456816',
email 		= 'CYNTHIA.YOUNG@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= 	 "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'HERNANDEZ',
first_name 	= 'ANGELA',
phone 		= '0123456817',
email 		= 'ANGELA.HERNANDEZ@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= 	 "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'KING',
first_name 	= 'MELISSA',
phone 		= '0123456818',
email 		= 'MELISSA.KING@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= 	 "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'WRIGHT',
first_name 	= 'BRENDA',
phone 		= '0123456819',
email 		= 'BRENDA.WRIGHT@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= 	 "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'LOPEZ',
first_name 	= 'AMY',
phone 		= '0123456820',
email 		= 'AMY.LOPEZ@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= 	 "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'HILL',
first_name 	= 'ANNA',
phone 		= '0123456821',
email 		= 'ANNA.HILL@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'SCOTT',
first_name 	= 'REBECCA',
phone 		= '0123456822',
email 		= 'REBECCA.SCOTT@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'GREEN',
first_name 	= 'VIRGINIA',
phone 		= '0123456823',
email 		= 'VIRGINIA.GREEN@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'ADAMS',
first_name 	= 'KATHLEEN',
phone 		= '0123456824',
email 		= 'KATHLEEN.ADAMS@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'BAKER',
first_name 	= 'PAMELA',
phone 		= '0123456825',
email 		= 'PAMELA.BAKER@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'GONZALEZ',
first_name 	= 'MARTHA',
phone 		= '0123456826',
email 		= 'MARTHA.GONZALEZ@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'NELSON',
first_name 	= 'DEBRA',
phone 		= '0123456827',
email 		= 'DEBRA.NELSON@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'CARTER',
first_name 	= 'AMANDA',
phone 		= '0123456828',
email 		= 'AMANDA.CARTER@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'MITCHELL',
first_name 	= 'STEPHANIE',
phone 		= '0123456829',
email 		= 'STEPHANIE.MITCHELL@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'PEREZ',
first_name 	= 'CAROLYN',
phone 		= '0123456830',
email 		= 'CAROLYN.PEREZ@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'ROBERTS',
first_name 	= 'CHRISTINE',
phone 		= '0123456831',
email 		= 'CHRISTINE.ROBERTS@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'TURNER',
first_name 	= 'MARIE',
phone 		= '0123456832',
email 		= 'MARIE.TURNER@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'PHILLIPS',
first_name 	= 'JANET',
phone 		= '0123456833',
email 		= 'JANET.PHILLIPS@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'CAMPBELL',
first_name 	= 'CATHERINE',
phone 		= '0123456834',
email 		= 'CATHERINE.CAMPBELL@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'PARKER',
first_name 	= 'FRANCES',
phone 		= '0123456835',
email 		= 'FRANCES.PARKER@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'EVANS',
first_name 	= 'ANN',
phone 		= '0123456836',
email 		= 'ANN.EVANS@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st2 = Student(
last_name 	= 'EDWARDS',
first_name 	= 'JOYCE',
phone 		= '0123456837',
email 		= 'JOYCE.EDWARDS@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp2,)
st2.save()
st3 = Student(
last_name 	= 'COLLINS',
first_name 	= 'DIANE',
phone 		= '0123456838',
email 		= 'DIANE.COLLINS@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'STEWART',
first_name 	= 'ALICE',
phone 		= '0123456839',
email 		= 'ALICE.STEWART@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'SANCHEZ',
first_name 	= 'JULIE',
phone 		= '0123456840',
email 		= 'JULIE.SANCHEZ@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'MORRIS',
first_name 	= 'HEATHER',
phone 		= '0123456841',
email 		= 'HEATHER.MORRIS@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'ROGERS',
first_name 	= 'TERESA',
phone 		= '0123456842',
email 		= 'TERESA.ROGERS@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'REED',
first_name 	= 'DORIS',
phone 		= '0123456843',
email 		= 'DORIS.REED@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'COOK',
first_name 	= 'GLORIA',
phone 		= '0123456844',
email 		= 'GLORIA.COOK@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'MORGAN',
first_name 	= 'EVELYN',
phone 		= '0123456845',
email 		= 'EVELYN.MORGAN@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'BELL',
first_name 	= 'JEAN',
phone 		= '0123456846',
email 		= 'JEAN.BELL@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'MURPHY',
first_name 	= 'CHERYL',
phone 		= '0123456847',
email 		= 'CHERYL.MURPHY@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'BAILEY',
first_name 	= 'MILDRED',
phone 		= '0123456848',
email 		= 'MILDRED.BAILEY@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'RIVERA',
first_name 	= 'KATHERINE',
phone 		= '0123456849',
email 		= 'KATHERINE.RIVERA@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'COOPER',
first_name 	= 'JOAN',
phone 		= '0123456850',
email 		= 'JOAN.COOPER@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
s1 = Student()
st3 = Student(
last_name 	= 'RICHARDSON',
first_name 	= 'ASHLEY',
phone 		= '0123456851',
email 		= 'ASHLEY.RICHARDSON@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'COX',
first_name 	= 'JUDITH',
phone 		= '0123456852',
email 		= 'JUDITH.COX@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'HOWARD',
first_name 	= 'ROSE',
phone 		= '0123456853',
email 		= 'ROSE.HOWARD@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'WARD',
first_name 	= 'JANICE',
phone 		= '0123456854',
email 		= 'JANICE.WARD@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'TORRES',
first_name 	= 'KELLY',
phone 		= '0123456855',
email 		= 'KELLY.TORRES@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'PETERSON',
first_name 	= 'NICOLE',
phone 		= '0123456856',
email 		= 'NICOLE.PETERSON@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'GRAY',
first_name 	= 'JUDY',
phone 		= '0123456857',
email 		= 'JUDY.GRAY@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'RAMIREZ',
first_name 	= 'CHRISTINA',
phone 		= '0123456858',
email 		= 'CHRISTINA.RAMIREZ@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'JAMES',
first_name 	= 'KATHY',
phone 		= '0123456859',
email 		= 'KATHY.JAMES@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'WATSON',
first_name 	= 'THERESA',
phone 		= '0123456860',
email 		= 'THERESA.WATSON@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st3 = Student(
last_name 	= 'BROOKS',
first_name 	= 'BEVERLY',
phone 		= '0123456861',
email 		= 'BEVERLY.BROOKS@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= "no comment",
cursus      = cp3,)
st3.save()
st4 = Student(
last_name 	= 'KELLY',
first_name 	= 'DENISE',
phone 		= '0123456862',
email 		= 'DENISE.KELLY@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'SANDERS',
first_name 	= 'TAMMY',
phone 		= '0123456863',
email 		= 'TAMMY.SANDERS@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'PRICE',
first_name 	= 'IRENE',
phone 		= '0123456864',
email 		= 'IRENE.PRICE@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'BENNETT',
first_name 	= 'JANE',
phone 		= '0123456865',
email 		= 'JANE.BENNETT@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'WOOD',
first_name 	= 'LORI',
phone 		= '0123456866',
email 		= 'LORI.WOOD@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'BARNES',
first_name 	= 'RACHEL',
phone 		= '0123456867',
email 		= 'RACHEL.BARNES@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'ROSS',
first_name 	= 'MARILYN',
phone 		= '0123456868',
email 		= 'MARILYN.ROSS@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'HENDERSON',
first_name 	= 'ANDREA',
phone 		= '0123456869',
email 		= 'ANDREA.HENDERSON@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'COLEMAN',
first_name 	= 'KATHRYN',
phone 		= '0123456870',
email 		= 'KATHRYN.COLEMAN@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'JENKINS',
first_name 	= 'LOUISE',
phone 		= '0123456871',
email 		= 'LOUISE.JENKINS@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'PERRY',
first_name 	= 'SARA',
phone 		= '0123456872',
email 		= 'SARA.PERRY@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'POWELL',
first_name 	= 'ANNE',
phone 		= '0123456873',
email 		= 'ANNE.POWELL@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'LONG',
first_name 	= 'JACQUELINE',
phone 		= '0123456874',
email 		= 'JACQUELINE.LONG@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'PATTERSON',
first_name 	= 'WANDA',
phone 		= '0123456875',
email 		= 'WANDA.PATTERSON@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'HUGHES',
first_name 	= 'BONNIE',
phone 		= '0123456876',
email 		= 'BONNIE.HUGHES@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'FLORES',
first_name 	= 'JULIA',
phone 		= '0123456877',
email 		= 'JULIA.FLORES@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'WASHINGTON',
first_name 	= 'RUBY',
phone 		= '0123456878',
email 		= 'RUBY.WASHINGTON@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'BUTLER',
first_name 	= 'LOIS',
phone 		= '0123456879',
email 		= 'LOIS.BUTLER@limayrac.fr',
birth_date 		= datetime(1999,12,17),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'SIMMONS',
first_name 	= 'TINA',
phone 		= '0123456880',
email 		= 'TINA.SIMMONS@limayrac.fr',
birth_date 		= datetime(1999,12,25),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'FOSTER',
first_name 	= 'PHYLLIS',
phone 		= '0123456881',
email 		= 'PHYLLIS.FOSTER@limayrac.fr',
birth_date 		= datetime(1999,12,18),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'GONZALES',
first_name 	= 'NORMA',
phone 		= '0123456882',
email 		= 'NORMA.GONZALES@limayrac.fr',
birth_date 		= datetime(1999,12,24),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'BRYANT',
first_name 	= 'PAULA',
phone 		= '0123456883',
email 		= 'PAULA.BRYANT@limayrac.fr',
birth_date 		= datetime(1999,12,19),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'ALEXANDER',
first_name 	= 'DIANA',
phone 		= '0123456884',
email 		= 'DIANA.ALEXANDER@limayrac.fr',
birth_date 		= datetime(1999,12,23),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'RUSSELL',
first_name 	= 'ANNIE',
phone 		= '0123456885',
email 		= 'ANNIE.RUSSELL@limayrac.fr',
birth_date 		= datetime(1999,12,20),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'GRIFFIN',
first_name 	= 'LILLIAN',
phone 		= '0123456886',
email 		= 'LILLIAN.GRIFFIN@limayrac.fr',
birth_date 		= datetime(1999,12,22),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'DIAZ',
first_name 	= 'EMILY',
phone 		= '0123456887',
email 		= 'EMILY.DIAZ@limayrac.fr',
birth_date 		= datetime(1999,12,21),
comments 	= "no comment",
cursus      = cp4,)
st4.save()
st4 = Student(
last_name 	= 'HAYES',
first_name 	= 'ROBIN',
phone 		= '0123456888',
email 		= 'ROBIN.HAYES@limayrac.fr',
birth_date 		= datetime(1999,12,26),
comments 	= "no comment",
cursus      = cp4,)
st4.save()

