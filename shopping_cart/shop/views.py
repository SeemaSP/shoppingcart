import json

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render,get_object_or_404

from .models import Country, State,City,Category,Product



class Getstates(View):
    """Class based view to get states related to country"""

    def get(self, request):

        """
        **Type:** public.

        **Arguments:**

            - request: Httprequest object.

        **Returns:** Dictionary containing  state details.

        **Raises:** Nothing.

        Following steps are performed in this method

        - Get country_id from request.GET.get('country_id').

        - Prepare an empty list say state_list.

        - Get states for country_id using.

        - for state in states
            - prepare a dictionary {"id": state.id, 'value': state.name}

            - append this dictionary to state_list.
        - Return state_list.
        """

        country_id = request.GET.get("country")
        list_states = []
        dict_states = {}
        # Get all active states from given country.
        country = get_object_or_404(Country, pk=country_id)
        states = country.state_set.order_by('name')
        for state in states:
            dict_states = {"id" : state.id, 'value' : state.name}
            list_states.append(dict_states)
        return HttpResponse(json.dumps(list_states))

class Getcities(View):
    """Class based view to get locations related to state"""

    def get(self, request):
        """
        **Type:** public.

        **Arguments:**

            - request: Http request object.

        **Returns:** Dictionary containing location details..

        **Raises:** Nothing.

        Following steps are performed in this method

        - Get state_id from *request.GET.get('state_id')*.

        - Prepare an empty list say *c*.

        - Get locations for *state_id*.

        - for location in locations
            - prepare a dictionary {"id": location.id, 'value': location.name}

            - append this dictionary to *location_list*.
        - Return location_list.
        """

        state_id = request.GET.get("state")
        list_cities = []
        dict_cities = {}
        # Get all active locations from given state.
        state = get_object_or_404(State, pk=state_id)
        cities = state.city_set.order_by('name')

        for city in cities:
            dict_cities = {"id" : city.id, 'value' : city.name}
            list_cities.append(dict_cities)
        return HttpResponse(json.dumps(list_cities))

		
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})
													  
def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    return render(request,'shop/product/detail.html',{'product': product})
