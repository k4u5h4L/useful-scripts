
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.io.Console;

public class Decrypt {

  Cipher ecipher;
  Cipher dcipher;

  Decrypt(SecretKey key) throws Exception {
    ecipher = Cipher.getInstance("AES");
    dcipher = Cipher.getInstance("AES");
    ecipher.init(Cipher.ENCRYPT_MODE, key);
    dcipher.init(Cipher.DECRYPT_MODE, key);
  }

  public String encrypt(String str) throws Exception {
    // Encode the string into bytes using utf-8
    byte[] utf8 = str.getBytes("UTF8");

    // Encrypt
    byte[] enc = ecipher.doFinal(utf8);

    // Encode bytes to base64 to get a string
    return new sun.misc.BASE64Encoder().encode(enc);
  }

  public String decrypt(String str) throws Exception {
    // Decode base64 to get bytes
    byte[] dec = new sun.misc.BASE64Decoder().decodeBuffer(str);

    byte[] utf8 = dcipher.doFinal(dec);

    // Decode using utf-8
    return new String(utf8, "UTF8");
  }


    public static void main(String args []) throws Exception
    {

        Console console = System.console();

        String k = new String(console.readPassword("Please enter your password: "));

        //SecretKey key = KeyGenerator.getInstance("AES").generateKey();
        SecretKey key = new SecretKeySpec(k.getBytes(), "AES");
        Decrypt encrypter = new Decrypt(key);

        String decrypted = encrypter.decrypt("9hEVQP8n0w4fH5S8SV7p59/FRNK4rcAdiv7/8EV7jysJTSVOQBtwjPPsw7Sovp1p");

        System.out.println("\nToken:\n" + decrypted);
    }
}