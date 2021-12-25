from django.shortcuts import render
from django.http import HttpResponse
from .myutils import countConsonant, countVocal
from time import ctime

day = {'Mon' : 'Senin',
       'Tue' : 'Selasa',
       'Wed' : 'Rabu',
       'Thu' : 'Kamis',
       'Fri' : 'Jumat',
       'Sat' : 'Sabtu',
       'Sun' : 'Minggu'}

month = {'Jan' : 'Januari',
       'Feb' : 'Februari',
       'Mar' : 'Maret',
       'Apr' : 'April',
       'May' : 'Mei',
       'Jun' : 'Juni',
       'Jul' : 'Juli',
       'Aug' : 'Agustus',
       'Sep' : 'September',
       'Oct' : 'Oktober',
       'Nov' : 'November',
       'Dec' : 'Desember'}


def code(request):
    time = ctime()
    hari = time[0:3]
    bulan = time[4:7]
    tanggal = time[8:10]
    tahun = time[20:24]
    jam = time[11:19]

    hari = day[hari]
    bulan = month[bulan]

    time = hari +' '+ tanggal +' '+ bulan +' '+ tahun +' '+ 'pukul ' + jam
    context = {
        'title' : 'TugasAP2021',
        'name' : 'Kurniawan Bagaskara',
        'nim' : 'L200214253',
        'time' : time,
        'message' : 'Kurniawan',
    }
    
    if request.POST:
        teks = request.POST.get('kalimat')
        vowel = countVocal(teks)
        consonant = countConsonant(teks)
        context.update( { 'kal' : teks,  
                        'vowels' : vowel,
                        'consonant' : consonant})
    

    return render(request, 'pajak/index.html', context)