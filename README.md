# Python ile RSA Şifreleme <br>
*Açık anahtarlı şifreleme algoritmasıdır.*<br><br>
**Şifreleme Adımları->**<br>
* İki adet asal sayı seçilir. ->(p,q)*<br>
* n = p.q yapılarak modulus bulunur.*<br>
* ->φ(n) = (p-1)(q-1) işlemi yapılarak totient değeri bulunur.<br>
* (1 < e < totient fonksiyon değeri) durumu ve seçilen e değerinin φ(n) ile aralarında asal olması şartıyla bir e değeri seçilir.<br>
* d.e ≡ 1 mod(φ(n)) hesaplanarak d değeri bulunur. Bu hesaplamayı yaparken öklit algoritmasından yararlanılır.<br>

**Karakteri şifreleme;->**<br>
* c = m^e mod(n) -> Şifrelenecek metin değeri: m , Modulus: n, Seçtiğimiz genel anahtar: e <br> 
