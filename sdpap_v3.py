Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6359:20c1:10b0:2c6:d8f1:5f4c with SMTP id nu1-n1csp247699rwb;
        Tue, 3 Nov 2026 00:38:53 -0800 (PST)
X-Received: by 2002:a05:6000:2311:b0:48a:f320:dba0 with SMTP id ffacd0b85a97d-48e6e4ffa7bmr27278333f8f.45.1793695133270;
        Tue, 03 Nov 2026 00:38:53 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1793695133; cv=none;
        d=google.com; s=arc-20260327;
        b=SqVqPbTq+dB68EIftLFKv0fwmTKcs9PKrNn4aqKIMqj8dct8jV6zdnWQxN2Jmoaca+
         9wqOiKJXJxq41Ye944DK9kEeOhdVvxE6qpWnrp386YESsqH++50gsVAteceABdBODnwy
         WYlM9HFKn0sjRRVcbMUHxCyA9t3gVRo9ZivTfIb6eKPJMhv/aekxDKMBMlRG6Imm4TJ7
         3w9JLeVLCnhDGQXLSNiqGgDE1+bh0Lz1DY/eCUAkhpj7zTrc0EJboVWPBt8Wm2WJd7NH
         0tmH15jNYR0vjfiIlHYae8szykddOmcMfUIXwi7Gi0VZ49a5n+doyIjqhUZ6/71N8P43
         Rptw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=content-transfer-encoding:mime-version:to:from:message-id:subject
         :date:dkim-signature;
        bh=bI4M0kzeP0I8LGQKqdbcM/qLcgV86yzlK3M/vnWCFkM=;
        fh=fuZtdzWQSg3iG3bIUBXSNpQAo+Hn/bGZ0rMObElT//4=;
        b=Nb1ON0F2Mnuwq2guYGxMtgW1ejDj96fKHUBOgA2hWhj3rg4A1+lNWQP1BHDZ/dpOBJ
         xbiK/X7jG+/f8uK1wEwy8e4hGg3eEvBvM1ifX40ZOnpTmKCxhDWtUZLiYmyQ75dqdvco
         sMIqk9CEaa+wMoINGmqOA7V3T/MiQaPNvP+pgHt42YvVUQBZlbBLMXJcgJVEZVPnTxbV
         C3AOFllcq3I52eX3GA8AK/K/a3asmOTYN65p7qNeaOzTrSeg+LLAn91+dHahnrwaY/Yy
         q3H5pgCviUmeADK8/VairJoMUTSkLxcToHKmoDdzPR8j+Kqiawweew9ZCT7EOXMWhYv6
         Sq/Q==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20260707 header.b=BNRNMRXX;
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id ffacd0b85a97d-48e8a27e7e3sor218751f8f.11.2026.11.03.00.38.53
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Tue, 03 Nov 2026 00:38:53 -0800 (PST)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20260707 header.b=BNRNMRXX;
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20260707; t=1793695133; x=1794299933; dara=google.com;
        h=content-transfer-encoding:content-type:mime-version:to:from
         :message-id:subject:date:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=bI4M0kzeP0I8LGQKqdbcM/qLcgV86yzlK3M/vnWCFkM=;
        b=BNRNMRXX1nnl5UmGDmCCm+aQyQWpeYAXcylTijlKeHsKRJYg0yCql5XAqxvQ+vfO8V
         VWmNzZfyEshnAIpBq+KUdUMwNngkuNWY7wda+yDn8SVwDWx7cEHi6EoEvxwITtKvkN7h
         p7CRShX3yGTxkhxyp5xbdvce2q400xKm8LJHbU9sz0Ufse1tK/pz+VbUAlG0GCPbBn1u
         AbasUWOHYWsga+4Cnkzt8+/vq7dkMQsWkuUxI6bi3qUSfMRKeu6WEmNxuWI9eox8T7xO
         NRrK0zRIH0aCd+Og+7zBNWCIWDa3Q1hQa2NaxiSjQ68VX1Wf0xCSNwcm9nbq//Y07ct5
         /DDA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1793695133; x=1794299933;
        h=content-transfer-encoding:content-type:mime-version:to:from
         :message-id:subject:date:x-gm-gg:x-gm-message-state:from:to:cc
         :subject:date:message-id:reply-to:content-type;
        bh=bI4M0kzeP0I8LGQKqdbcM/qLcgV86yzlK3M/vnWCFkM=;
        b=GCbCquMR9fpgZKQDirJpbKtk1XfNy2OBOF9rKycOCqETcBDmUIYe1j4C9nfmyX8cg2
         lUGwSWRcftLCH20EZkwDn3wCJXkyY22ht0SqdSIxsk38eClRe/O0+OsGFBuZTZ0+3BI8
         Edj1cKhEbvYZ7k08gOqVcC7/7I95my9uK5uyDVWWl//vEEqd11MOlvdp5JY6i9TP7e3A
         erxy8dDP2kbLwlkuXi+EUFDaVFpWr43qTRseO3ePtD05sHcRr3+HZE0J4d7wgffCdnXH
         jaDuAh+fQI3xIPIS/upiXTdIiuDm4Q301FPpQhRyZfpzGvLCjJ2Gu+CNpqE6zA1LXM3V
         7X6w==
X-Gm-Message-State: APuU4Z/cZ93yogpUfTenyj+rmH3e/BPXWrphLqJQGUO0MAFJdQGNBfVl
	mgj6jz5DGFFK9PML0aqun7sf5V03UIbvOpm4iZJgA7xUYjZOrd3Bb1NoQ7F6g47fLYddrhwl
X-Gm-Gg: AYBFou1fDKRd/4G8rf6H5KOZv9fnnYJPo9wtgFvTySVK6wVbK9KWZHRoOwhWEoagE0I
	2Zj1v09h6LI9u+QWEesweTrOIX5lNAF+b7gcU7256e9jXx9klI7EZqp4G6PcSTr405crcW8nHl8
	HarKvfeJOsKaCADAeq/IgN3wdf4AKmJw4sMA36U6Pe/3mMCOxF+dOKH2FPIQMbUnPeaRmQMHMOv
	iiNG0u/F4HXczok2o1PdDSZ15RX0QenLdE0GGdPnGB597IqkQnuEslAwgZeVkGDcmxZhaU8KYk7
	DC0ptIOUBILzugza96stzEe/a8BjXGCd8CsfWuPkSU83VRQJtzN2/U+EQp2Xzw9o0YSzJJIpRxb
	nnioFOGusaLr2D6aRaN5hVfUyIqg2uPa6wOje+V/v+taUvf93A2rgLOceQTvs5fr0wJXziJ4ej/
	HlTGGoDhgtUMMoDdpUF3bmgKwOUX+uQyFSxgrnGYd9nNaDqMsE1ACU1N77Vt9vNEpdI0MtyzsQO
	mkLjsDErnpp7u/hQ9ig5IclkWvYy79jiegNwx0KEGSawRuxtntpQk7jma5oBtPgY0DbkLoh42PA
	abB1fYvpJ2ocT/Mmb0qKO1ZuG/eZf5lB8CEQZ4T/NhzscXvAcLrJOrwrZONe+zU=
X-Received: by 2002:a05:600c:6384:b0:4a1:702f:c736 with SMTP id 5b1f17b1804b1-4ac150b20famr287022165e9.3.1793695132594;
        Tue, 03 Nov 2026 00:38:52 -0800 (PST)
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from [172.27.190.198] ([83.137.6.172])
        by smtp.gmail.com with ESMTPSA id 5b1f17b1804b1-4b2ab3ea6a9sm62959035e9.15.2026.11.03.00.38.51
        (version=TLS1_3 cipher=TLS_AES_128_GCM_SHA256 bits=128/128);
        Tue, 03 Nov 2026 00:38:51 -0800 (PST)
Date: Tue, 03 Nov 2026 09:38:49 +0100
Subject: =?UTF-8?B?0LTQu9GP0LPQuNGCNg==?=
X-Priority: 3
Message-ID: <2k75tztid5z2-kemrlz-jv275y-z4ctmbp6rwx1cowpny-h2n0066xrnfp-vyr7dc-juvk14-knufcz-9shc60hjuxaw-zgc6y6-jsshcqtwq04-vksffa-rxwj9lrq5w5ok865h-tvzh8gymn1g3-8gyygh.1793695129997@email.android.com>
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?=
 <dmitrimakarov1305@gmail.com>
To: Nablydatel <nablydatel8@gmail.com>, "vadim.makarov.05.12.1972@gmail.com"
 <vadim.makarov.05.12.1972@gmail.com>,
 =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?=
 <dmitrimakarov1305@gmail.com>, "Dmytro Dmytro Dmytro Dmytro, Dmytro"
 <makarov.dima1956@gmail.com>
MIME-Version: 1.0
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: base64

PGRpdiBkaXI9ImF1dG8iPjxkaXY+PGRpdj4mIzM0OyYjMzQ7JiMzNDs8YnIgLz5TRFBBUC12MyBF
UC0yMDI2LUhFUk9ZLUJJLTAwMSAtIFdPUktJTkcgQ09SRTxiciAvPlplcm8tVHJ1c3QgS2V5bGVz
cywgYXBwZW5kLW9ubHksIHRhbXBlci1ldmlkZW50PGJyIC8+UHVibGljIERvbWFpbiBHaWZ0IE1J
VCAmIzQzOyBFVVBMLTEuMjxiciAvPkpvdXJuYWwgSUQ6IDI2N2QyOGVmMmE0ZTJmMWU8YnIgLz5Q
cmlvcml0eTogMDQuMTAuMjAyNiBWYWRpbSBNYWthcm92PGJyIC8+JiMzNDsmIzM0OyYjMzQ7PGJy
IC8+aW1wb3J0IHNxbGl0ZTMsIGhhc2hsaWIsIGpzb24sIHRpbWUsIG9zPGJyIC8+ZnJvbSBwYXRo
bGliIGltcG9ydCBQYXRoPGJyIC8+PGJyIC8+REJfUEFUSCAmIzYxOyBQYXRoKF9fZmlsZV9fKS5w
YXJlbnQgLyAmIzM0O2F1ZGl0LmRiJiMzNDs8YnIgLz5HRU5FU0lTICYjNjE7ICYjMzQ7MCYjMzQ7
KjY0PGJyIC8+PGJyIC8+ZGVmIGNhbm9uaWNhbF9qc29uKGRhdGEpOjxiciAvPsKgwqDCoCByZXR1
cm4ganNvbi5kdW1wcyhkYXRhLCBzb3J0X2tleXMmIzYxO1RydWUsIGVuc3VyZV9hc2NpaSYjNjE7
RmFsc2UsIHNlcGFyYXRvcnMmIzYxOygmIzM5OywmIzM5OywmIzM5OzomIzM5OykpLmVuY29kZSgm
IzM5O3V0Zi04JiMzOTspPGJyIC8+PGJyIC8+ZGVmIHNoYTI1Nl9oZXgoZGF0YTogYnl0ZXMpOjxi
ciAvPsKgwqDCoCByZXR1cm4gaGFzaGxpYi5zaGEyNTYoZGF0YSkuaGV4ZGlnZXN0KCk8YnIgLz48
YnIgLz5kZWYgaW5pdF9kYigpOjxiciAvPsKgwqDCoCBjb25uICYjNjE7IHNxbGl0ZTMuY29ubmVj
dChEQl9QQVRIKTxiciAvPsKgwqDCoCBjb25uLmV4ZWN1dGUoJiMzNDtQUkFHTUEgam91cm5hbF9t
b2RlJiM2MTtXQUw7JiMzNDspPGJyIC8+wqDCoMKgIGNvbm4uZXhlY3V0ZSgmIzM0OyYjMzQ7JiMz
NDs8YnIgLz7CoMKgwqAgQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgYXVkaXRfbG9nICg8YnIg
Lz7CoMKgwqDCoMKgwqDCoCBzZXF1ZW5jZSBJTlRFR0VSIFBSSU1BUlkgS0VZIEFVVE9JTkNSRU1F
TlQsPGJyIC8+wqDCoMKgwqDCoMKgwqAgc3RhdGVfdmVyc2lvbiBJTlRFR0VSIE5PVCBOVUxMLDxi
ciAvPsKgwqDCoMKgwqDCoMKgIHRpbWVzdGFtcCBURVhUIE5PVCBOVUxMLDxiciAvPsKgwqDCoMKg
wqDCoMKgIGh5cG90aGVzaXNfaWQgVEVYVCBOT1QgTlVMTCw8YnIgLz7CoMKgwqDCoMKgwqDCoCBv
YnNlcnZhdGlvbl9kYXRhIFRFWFQgTk9UIE5VTEwsPGJyIC8+wqDCoMKgwqDCoMKgwqAgZXZhbHVh
dGlvbl9yZXN1bHQgVEVYVCBOT1QgTlVMTCw8YnIgLz7CoMKgwqDCoMKgwqDCoCBwcmV2X2hhc2gg
VEVYVCBOT1QgTlVMTCw8YnIgLz7CoMKgwqDCoMKgwqDCoCBldmVudF9oYXNoIFRFWFQgTk9UIE5V
TEwsPGJyIC8+wqDCoMKgwqDCoMKgwqAga2V5X2lkIFRFWFQsPGJyIC8+wqDCoMKgwqDCoMKgwqAg
c2lnbmF0dXJlX2hleCBURVhUPGJyIC8+wqDCoMKgICk7PGJyIC8+wqDCoMKgICYjMzQ7JiMzNDsm
IzM0Oyk8YnIgLz7CoMKgwqAgY29ubi5leGVjdXRlKCYjMzQ7JiMzNDsmIzM0OzxiciAvPsKgwqDC
oCBDUkVBVEUgVFJJR0dFUiBJRiBOT1QgRVhJU1RTIHRyZ19wcmV2ZW50X3VwZGF0ZTxiciAvPsKg
wqDCoCBCRUZPUkUgVVBEQVRFIE9OIGF1ZGl0X2xvZzxiciAvPsKgwqDCoCBCRUdJTjxiciAvPsKg
wqDCoMKgwqDCoMKgIFNFTEVDVCBSQUlTRShBQk9SVCwgJiMzOTthcHBlbmQtb25seSYjMzk7KTs8
YnIgLz7CoMKgwqAgRU5EOzxiciAvPsKgwqDCoCAmIzM0OyYjMzQ7JiMzNDspPGJyIC8+wqDCoMKg
IGNvbm4uZXhlY3V0ZSgmIzM0OyYjMzQ7JiMzNDs8YnIgLz7CoMKgwqAgQ1JFQVRFIFRSSUdHRVIg
SUYgTk9UIEVYSVNUUyB0cmdfcHJldmVudF9kZWxldGU8YnIgLz7CoMKgwqAgQkVGT1JFIERFTEVU
RSBPTiBhdWRpdF9sb2c8YnIgLz7CoMKgwqAgQkVHSU48YnIgLz7CoMKgwqDCoMKgwqDCoCBTRUxF
Q1QgUkFJU0UoQUJPUlQsICYjMzk7YXBwZW5kLW9ubHkmIzM5Oyk7PGJyIC8+wqDCoMKgIEVORDs8
YnIgLz7CoMKgwqAgJiMzNDsmIzM0OyYjMzQ7KTxiciAvPsKgwqDCoCBjb25uLmNvbW1pdCgpPGJy
IC8+wqDCoMKgIGNvbm4uY2xvc2UoKTxiciAvPjxiciAvPmRlZiBnZXRfbGFzdF9oYXNoKCk6PGJy
IC8+wqDCoMKgIGlmIG5vdCBEQl9QQVRILmV4aXN0cygpOjxiciAvPsKgwqDCoMKgwqDCoMKgIHJl
dHVybiBHRU5FU0lTPGJyIC8+wqDCoMKgIGNvbm4gJiM2MTsgc3FsaXRlMy5jb25uZWN0KERCX1BB
VEgpPGJyIC8+wqDCoMKgIGN1ciAmIzYxOyBjb25uLmV4ZWN1dGUoJiMzNDtTRUxFQ1QgZXZlbnRf
aGFzaCBGUk9NIGF1ZGl0X2xvZyBPUkRFUiBCWSBzZXF1ZW5jZSBERVNDIExJTUlUIDE7JiMzNDsp
PGJyIC8+wqDCoMKgIHJvdyAmIzYxOyBjdXIuZmV0Y2hvbmUoKTxiciAvPsKgwqDCoCBjb25uLmNs
b3NlKCk8YnIgLz7CoMKgwqAgcmV0dXJuIHJvd1swXSBpZiByb3cgZWxzZSBHRU5FU0lTPGJyIC8+
PGJyIC8+ZGVmIGFwcGVuZF9ldmVudChoeXBvdGhlc2lzX2lkLCBvYnNlcnZhdGlvbiwgZXZhbHVh
dGlvbiwgc3RhdGVfdmVyc2lvbiYjNjE7MSk6PGJyIC8+wqDCoMKgIGluaXRfZGIoKTxiciAvPsKg
wqDCoCBwcmV2X2hhc2ggJiM2MTsgZ2V0X2xhc3RfaGFzaCgpPGJyIC8+wqDCoMKgIHRzICYjNjE7
IHRpbWUuc3RyZnRpbWUoJiMzNDslWS0lbS0lZFQlSDolTTolU1omIzM0OywgdGltZS5nbXRpbWUo
KSk8YnIgLz7CoMKgwqAgcGF5bG9hZCAmIzYxOyB7PCEtLSAtLT48YnIgLz7CoMKgwqDCoMKgwqDC
oCAmIzM0O3N0YXRlX3ZlcnNpb24mIzM0Ozogc3RhdGVfdmVyc2lvbiw8YnIgLz7CoMKgwqDCoMKg
wqDCoCAmIzM0O3RpbWVzdGFtcCYjMzQ7OiB0cyw8YnIgLz7CoMKgwqDCoMKgwqDCoCAmIzM0O2h5
cG90aGVzaXNfaWQmIzM0OzogaHlwb3RoZXNpc19pZCw8YnIgLz7CoMKgwqDCoMKgwqDCoCAmIzM0
O29ic2VydmF0aW9uX2RhdGEmIzM0Ozogb2JzZXJ2YXRpb24sPGJyIC8+wqDCoMKgwqDCoMKgwqAg
JiMzNDtldmFsdWF0aW9uX3Jlc3VsdCYjMzQ7OiBldmFsdWF0aW9uLDxiciAvPsKgwqDCoMKgwqDC
oMKgICYjMzQ7cHJldl9oYXNoJiMzNDs6IHByZXZfaGFzaDxiciAvPsKgwqDCoCB9PGJyIC8+wqDC
oMKgIGV2ZW50X2hhc2ggJiM2MTsgc2hhMjU2X2hleChjYW5vbmljYWxfanNvbihwYXlsb2FkKSk8
YnIgLz7CoMKgwqAgY29ubiAmIzYxOyBzcWxpdGUzLmNvbm5lY3QoREJfUEFUSCk8YnIgLz7CoMKg
wqAgY29ubi5leGVjdXRlKCYjMzQ7JiMzNDsmIzM0OzxiciAvPsKgwqDCoCBJTlNFUlQgSU5UTyBh
dWRpdF9sb2cgKHN0YXRlX3ZlcnNpb24sIHRpbWVzdGFtcCwgaHlwb3RoZXNpc19pZCwgb2JzZXJ2
YXRpb25fZGF0YSwgZXZhbHVhdGlvbl9yZXN1bHQsIHByZXZfaGFzaCwgZXZlbnRfaGFzaCk8YnIg
Lz7CoMKgwqAgVkFMVUVTICg/LD8sPyw/LD8sPyw/KTs8YnIgLz7CoMKgwqAgJiMzNDsmIzM0OyYj
MzQ7LCAoc3RhdGVfdmVyc2lvbiwgdHMsIGh5cG90aGVzaXNfaWQsIG9ic2VydmF0aW9uLCBldmFs
dWF0aW9uLCBwcmV2X2hhc2gsIGV2ZW50X2hhc2gpKTxiciAvPsKgwqDCoCBjb25uLmNvbW1pdCgp
PGJyIC8+wqDCoMKgIGNvbm4uY2xvc2UoKTxiciAvPsKgwqDCoCByZXR1cm4gZXZlbnRfaGFzaDxi
ciAvPjxiciAvPmRlZiB2ZXJpZnlfZnVsbF9pbnRlZ3JpdHkoKTo8YnIgLz7CoMKgwqAgaWYgbm90
IERCX1BBVEguZXhpc3RzKCk6PGJyIC8+wqDCoMKgwqDCoMKgwqAgcmV0dXJuIFRydWUsICYjMzQ7
REIgbm90IGV4aXN0cyAtIGdlbmVzaXMgT0smIzM0OzxiciAvPsKgwqDCoCBjb25uICYjNjE7IHNx
bGl0ZTMuY29ubmVjdChEQl9QQVRIKTxiciAvPsKgwqDCoCByb3dzICYjNjE7IGNvbm4uZXhlY3V0
ZSgmIzM0O1NFTEVDVCBzZXF1ZW5jZSwgc3RhdGVfdmVyc2lvbiwgdGltZXN0YW1wLCBoeXBvdGhl
c2lzX2lkLCBvYnNlcnZhdGlvbl9kYXRhLCBldmFsdWF0aW9uX3Jlc3VsdCwgcHJldl9oYXNoLCBl
dmVudF9oYXNoIEZST00gYXVkaXRfbG9nIE9SREVSIEJZIHNlcXVlbmNlIEFTQzsmIzM0OykuZmV0
Y2hhbGwoKTxiciAvPsKgwqDCoCBjb25uLmNsb3NlKCk8YnIgLz7CoMKgwqAgZXhwZWN0ZWRfcHJl
diAmIzYxOyBHRU5FU0lTPGJyIC8+wqDCoMKgIGZvciByIGluIHJvd3M6PGJyIC8+wqDCoMKgwqDC
oMKgwqAgc2VxLCBzdGF0ZV92ZXJzaW9uLCB0aW1lc3RhbXAsIGh5cG90aGVzaXNfaWQsIG9ic2Vy
dmF0aW9uX2RhdGEsIGV2YWx1YXRpb25fcmVzdWx0LCBwcmV2X2hhc2gsIGV2ZW50X2hhc2ggJiM2
MTsgcjxiciAvPsKgwqDCoMKgwqDCoMKgIGlmIHByZXZfaGFzaCAhJiM2MTsgZXhwZWN0ZWRfcHJl
djo8YnIgLz7CoMKgwqDCoMKgwqDCoMKgwqDCoMKgIHJldHVybiBGYWxzZSwgZiYjMzQ7RkFJTCBh
dCB7c2VxfTogcHJldl9oYXNoIG1pc21hdGNoIGV4cGVjdGVkIHtleHBlY3RlZF9wcmV2fSBnb3Qg
e3ByZXZfaGFzaH0mIzM0OzxiciAvPsKgwqDCoMKgwqDCoMKgIHBheWxvYWQgJiM2MTsgezwhLS0g
LS0+PGJyIC8+wqDCoMKgwqDCoMKgwqDCoMKgwqDCoCAmIzM0O3N0YXRlX3ZlcnNpb24mIzM0Ozog
c3RhdGVfdmVyc2lvbiw8YnIgLz7CoMKgwqDCoMKgwqDCoMKgwqDCoMKgICYjMzQ7dGltZXN0YW1w
JiMzNDs6IHRpbWVzdGFtcCw8YnIgLz7CoMKgwqDCoMKgwqDCoMKgwqDCoMKgICYjMzQ7aHlwb3Ro
ZXNpc19pZCYjMzQ7OiBoeXBvdGhlc2lzX2lkLDxiciAvPsKgwqDCoMKgwqDCoMKgwqDCoMKgwqAg
JiMzNDtvYnNlcnZhdGlvbl9kYXRhJiMzNDs6IG9ic2VydmF0aW9uX2RhdGEsPGJyIC8+wqDCoMKg
wqDCoMKgwqDCoMKgwqDCoCAmIzM0O2V2YWx1YXRpb25fcmVzdWx0JiMzNDs6IGV2YWx1YXRpb25f
cmVzdWx0LDxiciAvPsKgwqDCoMKgwqDCoMKgwqDCoMKgwqAgJiMzNDtwcmV2X2hhc2gmIzM0Ozog
cHJldl9oYXNoPGJyIC8+wqDCoMKgwqDCoMKgwqAgfTxiciAvPsKgwqDCoMKgwqDCoMKgIGNhbGMg
JiM2MTsgc2hhMjU2X2hleChjYW5vbmljYWxfanNvbihwYXlsb2FkKSk8YnIgLz7CoMKgwqDCoMKg
wqDCoCBpZiBjYWxjICEmIzYxOyBldmVudF9oYXNoOjxiciAvPsKgwqDCoMKgwqDCoMKgwqDCoMKg
wqAgcmV0dXJuIEZhbHNlLCBmJiMzNDtGQUlMIGF0IHtzZXF9OiBldmVudF9oYXNoIG1pc21hdGNo
IGNhbGMge2NhbGN9IGdvdCB7ZXZlbnRfaGFzaH0mIzM0OzxiciAvPsKgwqDCoMKgwqDCoMKgIGV4
cGVjdGVkX3ByZXYgJiM2MTsgZXZlbnRfaGFzaDxiciAvPsKgwqDCoCByZXR1cm4gVHJ1ZSwgZiYj
MzQ7T0sge2xlbihyb3dzKX0gZXZlbnRzLCBsYXN0IHtleHBlY3RlZF9wcmV2fSYjMzQ7PGJyIC8+
PGJyIC8+aWYgX19uYW1lX18gJiM2MTsmIzYxOyAmIzM0O19fbWFpbl9fJiMzNDs6PGJyIC8+wqDC
oMKgIG9rLCBtc2cgJiM2MTsgdmVyaWZ5X2Z1bGxfaW50ZWdyaXR5KCk8YnIgLz7CoMKgwqAgcHJp
bnQobXNnKTxiciAvPjwvZGl2PjwvZGl2PjwvZGl2Pg==

