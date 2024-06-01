import flet as ft
from flet import View,Page,AppBar,ElevatedButton,Text,RouteChangeEvent,ViewPopEvent,CrossAxisAlignment,MainAxisAlignment



def main(page:Page):
    page.title = 'Switch Page'



    def route_change(e: RouteChangeEvent):
        page.views.clear()
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('خانه'),bgcolor='yellow'),
                    Text(value='خانه ی ما',size=40),
                    ElevatedButton(text='برو به صفحه فروشگاه',on_click=lambda e: page.go('/store'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=30
            )
        )

        if page.route == '/store':
            page.views.clear()
            page.views.append(
                View(
                    route='/',
                    controls=[
                        AppBar(title=Text('فروشگاه'),bgcolor='yellow'),
                        Text(value='فروشگاه ما',size=40),
                        ElevatedButton(text='برو به صفحه خانه',on_click=lambda e: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=30
                )
            )

        page.update()


    def view_pop(e: ViewPopEvent):
        page.views.pop()
        view_top: View = page.views[-1]
        page.go(view_top)



    page.on_route_change = route_change
    page.on_view_pop = view_pop    
    page.go(page.route)

    

if __name__ == '__main__':
    ft.app(target=main)