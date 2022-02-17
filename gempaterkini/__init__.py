import requests
from bs4 import BeautifulSoup
"""
Method = fungsi
Field / Atribute = variabel
"""
class gempaterkini:
    def __init__(self, url):
        self.description = 'To get the latest earthquake in Indonesia from BMKG.go.id'
        self.result = None
        self.url = url

    def ekstrasi_data(self):
        """
        Tanggal: 04 Februari 2022
        Waktu: 17:10:45 WIB
        Magnitudo: 5.5
        Kedalaman: 10 km
        Lokasi: LS=7.48 LS - BT=105.92 BT
        Pusat gempa: Pusat gempa berada di laut 71 Km Barat Daya Bayah
        Dirasakan: Dirasakan (Skala MMI): IV Pelabuhan Ratu, III Malingping, III Bayah, III Cihara, III Panggarangan
        :return:
        """
        try:
            content = requests.get(self.url)
        except Exception:
            return None

        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser')

            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            waktu = result[1]
            tanggal = result[0]

            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')
            i = 0
            magnitudo = None
            kedalaman = None
            ls = None
            bt = None
            lokasi = None
            keterangan = None

            for res in result:
                if i == 1:
                    magnitudo = res.text
                elif i == 2:
                    kedalaman = res.text
                elif i == 3:
                    koordinat = res.text.split(' - ')
                    ls = koordinat [0]
                    bt = koordinat [1]
                elif i == 4:
                    lokasi = res.text
                elif i == 5:
                    keterangan = res.text
                i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls': ls, 'bt': bt }
            hasil['lokasi'] = lokasi
            hasil['keterangan'] = keterangan
            self.result = hasil
        else:
            return None


    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data gempa terkini")
            return

        print('Gempa terakhir berdasarkan BMKG')
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo: {self.result['magnitudo']}")
        print(f"Kedalaman: {self.result['kedalaman']}")
        print(f"Koordinat: LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"Lokasi: {self.result['lokasi']}")
        print(f"Keterangan: {self.result['keterangan']}")

    def run(self):
        self.ekstrasi_data()
        self.tampilkan_data()

if __name__ == '__main__':
    gempa_di_indonesia = gempaterkini('https://bmkg.go.id')
    print('Deskripsi class gempaterkini', gempa_di_indonesia.description)
    gempa_di_indonesia.run()

    gempa_di_dunia = gempaterkini('https://bmkg.go.id')
    print('Deskripsi class gempaterkini', gempa_di_dunia.description)
    gempa_di_dunia.run()
    # gempa_di_indonesia.ekstrasi_data()
    # gempa_di_indonesia.tampilkan_data()