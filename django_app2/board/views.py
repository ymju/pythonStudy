from django.shortcuts import render, redirect

from board.models import Board


def boardList(request):
    return render(request, 'boardList.html', {'list':Board.objects.all()} )

def writePage(request):
    return render(request, 'writePage.html', {})

def write(request):
    Board.objects.create(
        subject=request.POST['subject'],
        content=request.POST['content']
    ).save()
    return redirect('/list')

def detail(request, pk):
    board = Board.objects.get(id=pk)
    board.viewCount += 1
    board.save()
    return render(request, 'boardDetail.html', {'board':Board.objects.get(id=pk)})