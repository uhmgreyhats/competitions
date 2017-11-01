# TomCrypt

Tom lost his decryption function, can you him out?

```
void enc(char* flag, byte key)
{
  while(*flag)
  {
    *flag^=(key=(key*13)+37);
    *(flag++) += 3;
  }
}
ciphertext: 3C F7 BF 3C D9 53 49 57 33 27 68 BA 70 28 65
```
