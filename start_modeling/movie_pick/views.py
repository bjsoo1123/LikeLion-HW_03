from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def name(request):
    return render(request, 'movie_pick/name.html')
    
    
def main(request):
    if request.method == "POST":
        name = request.POST.get('name')
        product = Product(name=name)
        product.save()
        # 그리고 변수 이름이 복수가 아니라 객체 하나니까 product라고 지어주는게 좋음
        # 그리고 redirect 는 return 안써주면 동작안함 그리고 쓸 필요도없음 여기선
        # 여기서 이제 이름을 받아서 바로 product 객체를 하나 생성할거임
        # 이렇게 하면 main에서 이름을 입력받고 바로 product 객체를 생성함 
    return render(request, 'movie_pick/main.html', {'product': product})
    ## dictionary_type : name이라는 key에 name의 value를 취한다.
    # 자그럼 이제 main 에서 값들을 form 으로 던져주잖아 interesting 으로 ㅇㅋ?
    # 그걸 이제 interesting 에서 받아서 처리를 할건데 그전에 해당 product 객체를 찾으려면
    # main.html 에서 pk 를 input hidden type으로 던져줘야함 그래서 main.html 와보셈
    

def interesting(request):
    if request.method == "POST":
        pk = request.POST.get('pk')# 아 main.html에서 이거 이름을 안 정해줬으니까 정해주자
        product = get_object_or_404(Product, pk=id)# 이제 pk 를 받았으니까 이걸로 찾을거야 객체를
        # 이제 이 객체를 찾았으니까 이걸 이용해서 사용하면됨
        movie = request.POST.get('movie')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        product.movie = movie
        product.genre = genre
        product.description = description
        product.save()
        # 자 이렇게 하면 product 객체를 찾고 그 객체의 movie, genre 등등을 request.POST 로 날라온 값으로 변경해주고 저장한느거임
        # 그리고 이 수정한 객체를 그대로 product 를 넘겨주니까 바로 쓸수 있겠지 interesting.html 로오삼
    return render(request, 'movie_pick/interesting.html', {'product': product})
    
    
def list(request):
    products = Product.objects.all()
    return render(request, 'movie_pick/list.html', {'all_products': products})
    

# 상세 페이지 구현    
def show(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'movie_pick/show.html', {'product': product})
    
    
def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'movie_pick/edit.html', {'product': product})
    
    
def update(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        movie = request.POST.get('movie')
        genre = request.POST.get('genre')
        discription = request.POST.get('discription')
        product.movie = movie
        product.genre = genre
        product.discription = discription
        product.save()
        return redirect('products:list')
        

def delete(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        product.delete()
    return redirect('products:list')