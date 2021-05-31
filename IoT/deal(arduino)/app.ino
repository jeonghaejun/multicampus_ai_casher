#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN   9
#define SS_PIN   10


MFRC522 mfrc(SS_PIN, RST_PIN);

void setup()
{
	Serial.begin(9600);
    SPI.begin();
    mfrc.PCD_Init();
}

void loop()
{
	if ( !mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial() ) {
        delay(500);
        return;
    }

    Serial.print("Card UID:");

    for (byte i = 0; i < 4; i++) {
        Serial.print(mfrc.uid.uidByte[i]);
        Serial.print(" ");
    }
    Serial.println();
}
