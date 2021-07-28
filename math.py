from manim import *
import numpy as np
import scipy.integrate as integrate

def intg(a, b):
        #func = lambda x : np.abs(x)*np.cos(x)*np.sin(x)
        func = lambda x : np.sin(x)
        return (integrate.quad(func,a,b))[0]   
        

class Graphs(Scene):
    def construct(self):
        axes = Axes(x_range=[-5,12],y_range=[-5,8])
        self.add(axes.add_coordinates())

        self.play(Write(axes, lag_ratio = 0.01,run_time = 2))
        t=ValueTracker(50)

        #graph = axes.get_graph(lambda x : np.abs(x)*np.cos(x)*np.sin(x), color = BLUE)
        #label = axes.get_graph_label(graph, "\int_{1}^{6} |x|cos(x)sin(x) dx").to_edge(UR)

        graph = axes.get_graph(lambda x : np.sin(x), color = BLUE)
        label = axes.get_graph_label(graph, "\int_{1}^{6.2381} sin(x) dx").to_edge(UR)

        self.play(Create(graph),FadeIn(label), lag_ratio = 0.01, run_time = 2)
        
        rects = axes.get_area(graph,[0,6.2831],dx_scaling=30)
        rects.add_updater(lambda x: x.become(axes.get_area(graph,[0,6.2831],dx_scaling=t.get_value())))
        self.play(Create(rects),run_time = 2)
        self.play(t.animate(run_time=4,rate_func=linear).set_value(1))
        
        answer = intg(0,6.2831)
        self.play(Write(DecimalNumber(
            answer, 
            num_decimal_places=5, 
            include_sign=True, 
            show_ellipsis=True
            ).to_corner(UR).shift(DOWN*2)))
        self.wait(5)

