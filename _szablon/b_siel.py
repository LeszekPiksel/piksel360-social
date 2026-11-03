from kit import *
P='photos/'; R=SITE+'realizacje/www/'
T='Realizacja · Strona www'; F='Osada Sielankowo · <b>sielankowo.eu</b>'; N=5
jobs=[
 ('sielankowo-1', s_hero(P+'jacuzzi.jpg','Nowa realizacja','Osada Sielankowo','Strona dla domów nad jeziorem w Kleszczynie i Kopcu',T,F,1,N,
   extra=phone(R+'sielankowo-mobile.webp',770,250,470,4,off=203))),
 ('sielankowo-2', s_features(P+'rodzina.jpg','Co jest na stronie','Wszystko, czego szuka gość',[
   ('home','Karta każdego domu','opis, wyposażenie, cennik i galeria'),
   ('pin','Dwie lokalizacje osobno','gość od razu wie, co wybiera'),
   ('news','Aktualności','ściągają ludzi z Google'),
   ('phone','Rezerwacja jednym kliknięciem','także z telefonu')],T,F,2,N,pos='center 40%')),
 ('sielankowo-3', s_mockup(P+'okno.jpg',R+'sielankowo-desktop.webp',R+'sielankowo-mobile.webp','sielankowo.eu','Komputer i telefon','Wygląda świetnie<br>na każdym ekranie',T,F,3,N,doff=46,moff=203)),
 ('sielankowo-4', s_collage([P+'trawa.jpg',P+'wino.jpg',P+'okno.jpg'],'Zdjęcia grają pierwsze skrzypce','Duże zdjęcia, mało tekstu.<br><span class="lime">Klimat czuć od razu.</span>',T,F,4,N)),
 ('sielankowo-5', s_cta(P+'jacuzzi.jpg','Twoja firma też zasługuje na <span class="lime">taką stronę</span>','Strona, która pracuje na Ciebie, a nie tylko wisi w sieci. Porozmawiajmy o Twojej.',T,'Piksel360 · <b>webowe systemy dla firm</b>',5,N)),
]
print(render(jobs,'out/04-sielankowo'))
