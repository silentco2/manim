from manim import *


class Intro(Scene):
    def construct(self):
        intro = Tex("Hello World", " this is Osama")
        intro[0].set_color(GREEN)
        intro[1].set_color(LIGHT_BROWN)
        t = Text("welcome to this course about Algorithms analysis and design", color=RED, font_size=35)
        self.play(Write(VGroup(intro, t).arrange(DOWN)), run_time=5)


class Define(Scene):
    def construct(self):
        definition = VGroup(Text("Algorithm is one of the most important pillars of computer science.", font_size=27, color=BLUE),
                            Text("it can be considered as an approach to think how to solve the problem efficiently", font_size=27, color=BLUE),
                            Text("in simple terms we can define an algorithm as follows:", font_size=30, color=YELLOW),
                            Text("Number of steps that give you the solution of a desired problem", font_size=30, color=YELLOW),
                            Text("so we can deduce that an algorithm is not limited to computer scientists only\nbut can be used in any other field because its a way of thinking", font_size=27, color=BLUE)).arrange(DOWN)
        definition[0].to_edge(UP)
        definition[1].to_edge(LEFT).next_to(definition[0], DOWN)
        definition[2].to_edge(LEFT)
        definition[3].to_edge(LEFT)
        definition[4].to_edge(DL)
        self.play(Write(definition[:2]), run_timr=4)
        self.wait(4)
        self.play(Write(definition[2:4]), run_timr=4)
        self.wait(4)
        self.play(Write(definition[4]), run_timr=4)
        self.wait(4)


class S1(Scene):
    def construct(self):
        definition = VGroup(Text("Before you go on and begin designing algorithms, you should learn how to analyze them", font_size=25, color=BLUE),
                            Text("this is to make sure that you understand what is the cost of some solutions", font_size=25, color=BLUE),
                            Text("Analyzing an algorithm is math based so we need to put some ground rules", font_size=30, color=ORANGE),
                            Tex("induction,", "logarithms,", "exponents,", "asymptotic analysis", font_size=30),
                            Text("when we say analyzing an algorithm we don't target the algorithm itself \ninstead we mean the implementation of such algorithm", font_size=27, color=BLUE)).arrange(DOWN)
        definition[0].to_edge(UP)
        definition[1].to_edge(LEFT).next_to(definition[0], DOWN)
        definition[2].to_edge(LEFT)
        definition[3].to_edge(LEFT)
        definition[4].to_edge(DL)
        definition[3][0].set_color(RED)
        definition[3][1].set_color(GREEN)
        definition[3][2].set_color(BLUE)
        definition[3][3].set_color(YELLOW)
        self.play(Write(definition[:2]), run_timr=4)
        self.wait(4)
        self.play(Write(definition[2:4]), run_timr=4)
        self.wait(4)
        self.play(Write(definition[4]), run_timr=4)
        self.wait(4)


class S2(Scene):
    def construct(self):
        definition = VGroup(Text("Induction", font_size=30),
                            Tex("Theorem:\:", r"$$\sum_{x=1}^{n}x\:=\:\frac{n(n+1)}{2}$$", font_size=40, color=RED),
                            Tex("get\:the\:base\:case:\:at\:n\:=\:1", r"$$\sum_{x=1}^{n}x\:=\:1\:and\:\frac{1(1+1)}{2}\:=\:1$$", font_size=30, color=GREEN),
                            Tex("get\:the\:inductive\:case:\:at\;n\:=\:k", r"$$\because\sum_{x=1}^{n+1}x\:=\:\sum_{x=1}^{n}x\:+\:(n+1)$$", r"$\therefore\frac{(n+1)(n+2)}{2}\:=\:\frac{n(n+1)}{2}+n+1$", color=BLUE, font_size=30),
                            Tex("proof:\:", r"$\frac{(n+1)(n+2)}{2}\:=\:$", font_size=35),
                            Tex(r"$\frac{n(n+1)}{2}$", "+(n+1)", r"$+\frac{2(n+1)}{2}$", r"$\frac{n(n+1)+2(n+1)}{2}$", r"$\frac{n^{2}+n+2n+2}{2}$", r"$\frac{n^{2}+3n+2}{2}$", font_size=35).arrange(ORIGIN))
        definition[0].to_edge(UP)
        definition[1].to_edge(LEFT).next_to(definition[0], DOWN)
        definition[3].to_edge(RIGHT)
        definition[2].to_edge(LEFT)
        definition[4].set_y(-2).set_x(-2)
        definition[5].next_to(definition[4], RIGHT)
        definition[5][1].next_to(definition[5][0], RIGHT)
        definition[5][2].next_to(definition[5][0], RIGHT)
        self.play(Write(definition[:2]), run_timr=4)
        self.wait(2)
        self.play(Write(definition[2]), run_timr=4)
        self.wait(2)
        self.play(Write(definition[3]), run_timr=4)
        self.wait(4)
        self.play(Write(definition[4]), run_timr=4)
        self.play(Write(definition[5][0:2]), run_timr=4)
        self.wait(2)
        self.play(ReplacementTransform(definition[5][1], definition[5][2]))
        self.wait(2)
        self.play(ReplacementTransform(definition[5][0:3], definition[5][3]))
        self.wait(2)
        self.play(ReplacementTransform(definition[5][3], definition[5][4]))
        self.wait(2)
        self.play(ReplacementTransform(definition[5][4], definition[5][5]))
        self.wait(3)


class S3(Scene):
    def construct(self):
        definition = VGroup(Text("Logarithms and Exponents", font_size=30, color=BLUE),
                            Tex("because computer use binary in everything when we say$\:\log n$ we almost always mean $\log _{2} n$", font_size=35, color=BLUE),
                            Text("properties of logarithms and exponents are very important\nthe two most important to know", font_size=27, color=ORANGE),
                            Tex(r"-\:let$\:\log _{2}x\:=\:y$", font_size=35),
                            Tex(r"$\therefore 2^{y}=x$", font_size=35),
                            Tex("-\:$2^{log _{2}x}=x$", font_size=35)).arrange(DOWN)
        definition[0].to_edge(UP)
        definition[1].to_edge(LEFT).next_to(definition[0], DOWN)
        definition[2].to_edge(LEFT)
        definition[4].next_to(definition[3], RIGHT)
        definition[3:6].set_y(-2)
        self.play(Write(definition[:2]), run_timr=4)
        self.wait(2)
        self.play(Write(definition[2]), run_timr=4)
        self.play(Write(definition[3]))
        self.wait(1)
        self.play(Write(definition[4]))
        self.wait(1)
        self.play(Write(definition[5]), run_timr=4)
        self.wait(2)


class S4(Scene):
    def construct(self):
        definition = VGroup(Text("Asymptotic Analysis", font_size=30, color=RED),
                            Text("you are already familiar with big O notation, but do you know how it came to be", font_size=27,color=ORANGE),
                            Text("Let's try to analyze this code and come with the exact time complexity", font_size=27, color=BLUE),
                            Code(code="for(int i=0;i<=n;i++){\nx=x+1\n}", tab_width=4, language="Java", font="Monospace"),
                            Text("every operation counts while analyzing an algorithm ", font_size=27, color=YELLOW),
                            Text("but don't worry we needn't be exact, as we only need the most significant term\nalso without it's coefficient", font_size=27, color=PURPLE)).arrange(DOWN)
        tracker = ValueTracker(0)
        t1 = ValueTracker(0)
        iteration = Text("i = ", font_size=25).set_x(-4).set_y(1)
        worstcase = Text("Time Complexity = ", font_size=25).set_x(4).set_y(1)
        n = always_redraw(lambda: DecimalNumber(0, unit=None, num_decimal_places=0).set_value(t1.get_value()).next_to(iteration, RIGHT))
        decimal = always_redraw(lambda: DecimalNumber(0, unit=None, num_decimal_places=0).set_value(tracker.get_value()).next_to(worstcase, RIGHT))
        bigo = Text("4n+1", font_size=25).next_to(worstcase, RIGHT)
        definition[0].to_edge(UP)
        definition[1].next_to(definition[0], DOWN)
        definition[2].next_to(definition[1], DOWN)
        definition[5].to_edge(DOWN)
        definition[4].next_to(definition[5], UP)
        arrow = Arrow(start=UP, end=DOWN, buff=0.75).set_y(1)
        arrow2 = Arrow(start=UP, end=DOWN, buff=0.75).set_y(1).set_x(1)
        arrow3 = Arrow(start=UP, end=DOWN, buff=0.75).set_y(1).set_x(2)
        arrow4 = Arrow(start=RIGHT, end=LEFT, buff=0.75).set_y(-.2).set_x(-.5)
        nth = Text("n", font_size=25).next_to(iteration, RIGHT)
        self.play(Write(definition[:2]), run_timr=4)
        self.wait(2)
        self.play(Write(definition[2]))
        self.wait(3)
        self.play(Create(definition[3]), run_timr=4)
        self.wait(3)
        self.play(Create(arrow))
        self.play(FadeIn(worstcase, decimal, iteration, n))
        self.wait(1)
        tracker.set_value(1)
        self.wait(1)
        self.play(Transform(arrow, arrow2))
        self.wait(1)
        tracker.set_value(2)
        self.wait(1)
        self.play(Transform(arrow, arrow3))
        self.wait(1)
        tracker.set_value(3)
        self.wait(1)
        self.play(Transform(arrow, arrow4))
        self.wait(1)
        tracker.set_value(5)
        self.wait(1)
        t1.set_value(1)
        self.wait(1)
        self.play(Transform(arrow, arrow2))
        self.wait(1)
        tracker.set_value(6)
        self.wait(1)
        self.play(Transform(arrow, arrow3))
        self.wait(1)
        tracker.set_value(7)
        self.wait(1)
        self.play(Transform(arrow, arrow4))
        self.wait(1)
        tracker.set_value(9)
        self.wait(1)
        t1.set_value(2)
        self.wait(1)
        self.play(Transform(arrow, arrow2))
        self.play(ReplacementTransform(n, nth))
        self.wait(1)
        self.play(ReplacementTransform(decimal, bigo))
        self.wait(1)
        self.play(Write(definition[4]))
        self.wait(1)
        self.play(Write(definition[5]))
        self.wait(2)


class S5(Scene):
    def construct(self):
        definition = VGroup(Text("Recursion", font_size=35, color=BLUE),
                            Text("it's simply a function that recalls itself", font_size=25, color=BLUE),
                            Text("every recursive function is made of two main parts", font_size=27, color=ORANGE),
                            Tex("Base Case", font_size=30, color=RED),
                            Tex("Recursive Call", font_size=30, color=RED),
                            Tex("Change of parameters in a recursive call is needed to make sure that the recursion is not infinite", font_size=27, color=GREEN).arrange(DOWN))
        definition[0].to_edge(UP)
        definition[1].next_to(definition[0], DOWN)
        definition[3].next_to(definition[2], DL)
        definition[4].next_to(definition[2], DR)
        definition[5].to_edge(DOWN)
        self.play(Write(definition[:2]), run_timr=4)
        self.wait(2)
        self.play(Write(definition[2]), run_timr=3)
        self.wait(1)
        self.play(Write(definition[3]))
        self.wait(1)
        self.play(Write(definition[4]))
        self.wait(1)
        self.play(Write(definition[5]), run_timr=4)
        self.wait(2)


class S5andhalf(Scene):
    def construct(self):
        definition = VGroup(Text("Recursive Formula", font_size=30, color=BLUE),
                            Text("in order to understand and find the recursive functions time complexity", font_size=25, color=BLUE_E),
                            Text("we transform them to something called recursive formula, which basically is this", font_size=25, color=GREEN),
                            Text("complexity of function = complexity of recursive call + complexity of the base case", font_size=20),
                            Text("let that function be called T(n), and the case case is f(n)", font_size=25, color=YELLOW),
                            Text("then this formula can be rewritten into", font_size=25, color=ORANGE)).arrange(DOWN)
        formula = Text("T(n) = T(new parameter) + f(n)", font_size=20).next_to(definition[3]).set_x(0)
        definition[0].to_edge(UP)
        definition[1].set_y(2)
        definition[2].set_y(1)
        definition[4].set_y(-1)
        definition[5].set_y(-2)
        self.play(Write(definition[:2]))
        self.wait(1)
        self.play(Write(definition[2]))
        self.wait(3)
        self.play(Write(definition[3]))
        self.wait(1)
        self.play(Write(definition[4]))
        self.wait(1)
        self.play(Write(definition[5]))
        self.play(Transform(definition[3], formula))
        self.wait(1)


class S5andthreefourth(Scene):
    def construct(self):
        definition = VGroup(Text("Sum of The Time Complexity", font_size=30, color=YELLOW),
                            Text("loops are very tricky to find their complexity, so when looking at a loop try to find", font_size=25, color=ORANGE),
                            Text("Start", font_size=25, color=RED),
                            Text("Complexity of inner statements", font_size=25, color=GREEN),
                            Text("End", font_size=25, color=BLUE),
                            Text("to get the complexity of the loop write it in this form:", color=PURPLE, font_size=25),
                            Tex("$$\sum_{i=start}^{end}complexity\:of\:inner\:statements$$", font_size=25),
                            Text("although we speak mainly about loops this can be applied to recursive functions too", font_size=25, color=LIGHT_BROWN)).arrange(DOWN)
        formula = Text("T(n) = T(new parameter) + f(n)", font_size=20).next_to(definition[3]).set_x(0)
        definition[0].to_edge(UP)
        definition[1].next_to(definition[0], DOWN)
        definition[2].set_y(2)
        definition[3].set_y(1.25)
        definition[4].set_y(.5)
        definition[6].set_y(-2)
        definition[7].to_edge(DOWN)
        self.play(Write(definition[:2]))
        self.wait(1)
        self.play(Write(definition[2]))
        self.wait(2)
        self.play(Write(definition[3]))
        self.wait(1)
        self.play(Write(definition[4]))
        self.wait(1)
        self.play(Write(definition[5]))
        self.play(Write(definition[6]))
        self.wait(2)
        self.play(Write(definition[7]))
        self.wait(2)


class S6(Scene):
    def construct(self):
        definition = VGroup(Text("Example", font_size=30, color=BLUE),
                            Text("Get the time complexity of this recursive function", font_size=25, color=BLUE),
                            Code(code="fact(int n){\nif(n==0) return 1;\nelse return fact(n-1)*n;\n}", tab_width=4, language="Java", font="Monospace"),
                            Text("all statements are O(1)", font_size=20, color=GREEN),
                            Text("in the case of a conditional or a switch evaluate the complexity of each case and choose the biggest", font_size=20, color=BLUE),
                            Text("complexity of loops are the number of iterations * complexity of the inner statements", font_size=20, color=RED)).arrange(DOWN)
        title = Text("By Induction", font_size=30, color=RED).to_edge(UP).set_x(3)
        title1 = Text("base case n = 0, has a complexity of 1", font_size=25, color=ORANGE).next_to(title, DOWN).set_x(3)
        title2 = Text("let n = k, has complexity of 1+1+1+1...k times", font_size=25, color=YELLOW).next_to(title1, DOWN).set_x(3)
        formula1 = Text("recursive formula: ", font_size=25, color=ORANGE).next_to(title, DOWN).set_x(1.5)
        formula2 = Text("T (n) = T (n-1) + 1", font_size=25, color=YELLOW).next_to(title1, DOWN).set_x(4.5)
        t = VGroup(Text("then the complexity of this example is", font_size=27, color=GREEN),
                   Tex("$$\sum_{i=1}^{n}1$$", font_size=35),
                   Text("but how can we turn this summation into an actual value", font_size=27, color=GREEN),
                   Text("it all comes from sum of arithmetic and sum of geometric sequence", font_size=25, color=PINK),
                   Text("use arithmetic if the differance between consecutive terms is constant", font_size=25, color=RED_E),
                   Text("use geometric if the ratio between consecutive terms is constant", font_size=25, color=BLUE_E)).arrange(DOWN).set_y(-.5)
        arth = Tex(r"sum of arithmetic$$\sum_{i=a}^{n}\:=iterations\:(\frac{T_{a}+T_{n}}{2})$$", font_size=25).to_edge(LEFT).set_y(-3.3).generate_target()
        geo = Tex(r"sum of geometric$$\sum_{i=a}^{n}\:=\:\frac{T_{a}(r^{iterations}-1)}{r-1}$$", font_size=25).to_edge(RIGHT).set_y(-3.3)
        sumtitle = Text("Summation Rules Deduction", font_size=30, color=GREEN_A).to_edge(UP)
        sumrules = VGroup(Tex("$$\sum_{i=1}^{n}constant\:=\:$$", "$constant+constant+constant...n\:times$", "$$T_{a}=constant,\:T_{n}=constant,\:iterations=n$$", r"$$n(\frac{constant+constant}{2})$$", "$n\:*\:constant$", font_size=30),
        Tex("$$\sum_{i=1}^{n}i\:=\:$$", "1+2+3..+n", "$$T_{a}=1,\:T_{n}=n,\:iterations=n$$", r"$$n(\frac{1+n}{2})$$", font_size=30),
        Tex("$$\sum_{i=1}^{\log{n}}2^{i}\:=\:$$", "$2+4+8..+2^{n}$", "$$T_{a}=2,\:r=2,\:iterations=\log{n}$$", r"$$2(\frac{2^{\log{n}}-1}{2-1})$$", r"$2(\frac{n-1}{1})$", "$2(n-1)$", "$2n-1$", font_size=30),
        Tex("$$\sum_{i=1}^{n}i^{2}\:=\:$$", "$1+4+9..+n^{2}$", "the ratio here is not constant", r"$\frac{1}{4}\neq\frac{4}{9}$", "this is a power series", r"\\just use this for now", r"$\frac{n(n+1)(2n+1)}{6}$", font_size=30),
        Tex(r"$$\sum_{i=1}^{n}\frac{1}{i}\:=\:$$", r"$1+\frac{1}{2}+\frac{1}{3}..+\frac{1}{n}$", "this is a power series too!", "$\ln{n}+1$", font_size=30))
        for i in range(len(sumrules)):
            sumrules[i][0].to_edge(LEFT)
            for j in range(1, len(sumrules[i])):
                sumrules[i][j].next_to(sumrules[i][0], RIGHT)
        arth.generate_target()
        geo.generate_target()
        arth.target.to_edge(UL)
        geo.target.to_edge(UR)
        definition[0].to_edge(UP)
        definition[1].next_to(definition[0], DOWN)
        definition[5].to_edge(DOWN)
        definition[4].next_to(definition[5], UP)
        definition[3].next_to(definition[4], UP)
        formula1.generate_target()
        formula1.target.set_y(2.4)
        formula2.generate_target()
        formula2.target.set_y(2.4)
        definition[2].generate_target()
        definition[2].target.to_edge(UL)
        sumrules[1].set_y(0)
        sumrules[2].to_edge(RIGHT)
        sumrules[3].set_x(0).set_y(-1.5)
        sumrules[4].set_x(0).to_edge(DOWN)

        self.play(Write(definition[:2]), run_timr=4)
        self.wait(2)
        self.play(Create(definition[2]), run_timr=3)
        self.wait(1)
        self.play(Write(definition[3]))
        self.wait(1)
        self.play(Write(definition[4]))
        self.wait(1)
        self.play(Write(definition[5]), run_timr=4)
        self.wait(2)
        self.remove(definition[0], definition[1], definition[3], definition[4], definition[5])
        self.play(MoveToTarget(definition[2]))
        self.play(Write(title), Write(title1))
        self.wait(1)
        self.play(Write(title2))
        self.wait(1)
        self.play(Write(t[:3]))
        self.wait(2)
        self.play(ReplacementTransform(title1, formula1), ReplacementTransform(title2, formula2))
        self.play(MoveToTarget(formula1), MoveToTarget(formula2))
        self.wait(2)
        self.play(Write(t[3]))
        self.wait(1)
        self.play(Write(arth))
        self.play(Write(t[4]))
        self.wait(4)
        self.play(Write(geo))
        self.play(Write(t[5]))
        self.wait(4)
        self.remove(title, title1, title2, definition[2], t[0], t[1], t[2], t[3], t[4], t[5], formula1, formula2)
        self.play(MoveToTarget(arth), MoveToTarget(geo))
        self.play(Write(sumtitle))
        for i in range(len(sumrules)):
            self.play(Write(sumrules[i][0]))
            self.wait(2)
            self.play(Write(sumrules[i][1]))
            self.wait(2)
            for j in range(2, len(sumrules[i])):
                self.play(ReplacementTransform(sumrules[i][j-1], sumrules[i][j]))
                self.wait(3)


class S7(Scene):
    def construct(self):
        definition = VGroup(Text("Ways to solve recursion", font_size=30, color=ORANGE),
                            Text("not all recursive functions are directly or easily solved by induction", font_size=25, color=YELLOW),
                            Text("therefore we will discuss 3 of ways to find the complexity of such functions", font_size=25, color=PURPLE),
                            Text("Master Method", font_size=27, color=RED),
                            Text("Tree Method", font_size=27, color=GREEN),
                            Text("Substitution Method", font_size=27, color=BLUE)).arrange(DOWN)
        master = VGroup(Text("Derived from a concept called divide and conquer in which there are three main steps", font_size=25, color=GREEN),
                        Text("1) Divide", font_size=27, color=BLUE),
                        Text("2) Conquer", font_size=27, color=BLUE),
                        Text("3) Merge", font_size=27, color=BLUE),
                        Text("Merge Sort Example", font_size=27, color=GREEN)).arrange(DOWN)

        arr = VGroup().to_edge(LEFT)
        num = [38, 27, 43, 3, 9, 82, 10]
        for i in range(7):
            txt = Tex(str(num[i]), font_size=48)
            square = Square(side_length=1)
            txt.move_to(square.get_center())
            arr.add(VGroup(txt, square))
        arr.arrange(RIGHT, buff=0)

        definition[0].to_edge(UP)
        definition[1].next_to(definition[0], DOWN)
        definition[3].generate_target()
        definition[3].target.to_edge(UP)
        master[0].next_to(definition[3].target, DOWN)
        master[4].next_to(definition[3].target, DOWN)
        master[1].generate_target()
        master[2].generate_target()
        master[3].generate_target()
        master[1].target.set_y(2).set_x(-5)
        master[2].target.set_y(2)
        master[3].target.set_y(2).set_x(5)

        self.play(Write(definition[:2]), run_timr=4)
        self.wait(2)
        self.play(Write(definition[2]))
        self.wait(2)
        self.play(Write(definition[3]))
        self.wait(1)
        self.play(Write(definition[4]))
        self.wait(1)
        self.play(Write(definition[5]))
        self.wait(1)
        self.remove(definition[0], definition[1], definition[2], definition[4], definition[5])
        self.play(MoveToTarget(definition[3]))
        self.play(Write(master[0]))
        self.wait(1)
        self.play(Write(master[1]))
        self.play(Write(master[2]))
        self.play(Write(master[3]))
        self.play(MoveToTarget(master[1]), MoveToTarget(master[2]), MoveToTarget(master[3]))
        self.play(ReplacementTransform(master[0], master[4]))
        self.wait(2)
        self.play(Write(arr))
        self.wait(2)
        self.play(master[1].animate.set_color(GREEN_C), master[2].animate.set_color(GREY), master[3].animate.set_color(GREY))
        self.play(arr[:4].animate.shift(LEFT), arr[4:].animate.shift(RIGHT))
        self.wait(1)
        self.play(FadeOut(arr[4:]))
        self.wait(1)
        self.play(arr[:2].animate.shift(LEFT), arr[2:4].animate.shift(RIGHT))
        self.wait(1)
        self.play(master[1].animate.set_color(GREY), master[2].animate.set_color(GREEN_C))
        self.wait(1)
        self.play(Swap(arr[0], arr[1]))
        self.wait(1)
        self.play(Swap(arr[2], arr[3]))
        self.wait(2)
        self.play(arr[:4].animate.to_corner(DL))
        self.play(FadeIn(arr[4:]))
        self.wait(1)
        self.play(arr[4:6].animate.shift(LEFT), arr[6].animate.shift(RIGHT))
        self.wait(1)
        self.play(arr[4:].animate.to_corner(DR))
        self.wait(2)
        self.play(master[2].animate.set_color(GREY), master[3].animate.set_color(GREEN_C))
        self.play(arr[3].animate.set_color(RED), arr[1].animate.set_color(RED))
        self.wait(1)
        self.play(arr[3].animate.shift(UP*1.5 + LEFT*3).set_color(WHITE))
        self.wait(1)
        self.play(arr[2].animate.set_color(RED))
        self.wait(1)
        self.play(arr[1].animate.shift(UP * 1.5 + RIGHT * 2).set_color(WHITE))
        self.wait(1)
        self.play(arr[0].animate.set_color(RED))
        self.wait(1)
        self.play(arr[0].animate.shift(UP * 1.5 + RIGHT * 2).set_color(WHITE))
        self.wait(1)
        self.play(arr[2].animate.shift(UP * 1.5 + LEFT).set_color(WHITE))
        self.wait(2)
        self.play(arr[4].animate.set_color(RED), arr[6].animate.set_color(RED))
        self.wait(1)
        self.play(arr[4].animate.shift(UP * 1.5 + RIGHT).set_color(WHITE))
        self.wait(1)
        self.play(arr[5].animate.set_color(RED))
        self.wait(1)
        self.play(arr[6].animate.shift(UP * 1.5 + LEFT * 2).set_color(WHITE))
        self.wait(1)
        self.play(arr[5].animate.shift(UP * 1.5 + RIGHT * 2).set_color(WHITE))
        self.wait(1)
        self.play(arr[3].animate.set_color(RED), arr[4].animate.set_color(RED))
        self.wait(1)
        self.play(arr[3].animate.shift(UP * 1.5 + RIGHT * 2).set_color(WHITE))
        self.wait(1)
        self.play(arr[1].animate.set_color(RED))
        self.wait(1)
        self.play(arr[4].animate.shift(UP * 1.5 + LEFT * 5.25).set_color(WHITE))
        self.wait(1)
        self.play(arr[6].animate.set_color(RED))
        self.wait(1)
        self.play(arr[6].animate.shift(UP * 1.5 + LEFT * 5.25).set_color(WHITE))
        self.wait(1)
        self.play(arr[5].animate.set_color(RED))
        self.wait(1)
        self.play(arr[1].animate.shift(UP * 1.5 + RIGHT * 4).set_color(WHITE))
        self.wait(1)
        self.play(arr[0].animate.set_color(RED))
        self.wait(1)
        self.play(arr[0].animate.shift(UP * 1.5 + RIGHT * 4).set_color(WHITE))
        self.wait(1)
        self.play(arr[2].animate.set_color(RED))
        self.wait(1)
        self.play(arr[2].animate.shift(UP * 1.5 + RIGHT * 4).set_color(WHITE))
        self.wait(1)
        self.wait(1)
        self.play(arr[5].animate.shift(UP * 1.5 + LEFT * 2.25).set_color(WHITE))
        self.wait(2)
        self.play(FadeOut(arr))
        self.play(Unwrite(master[1]), Unwrite(master[2]), Unwrite(master[3]))
        self.play(Uncreate(master[4]))
        self.wait(1)
        # photo
        # self.add(definition[3], master, arr)


class S8(Scene):
    def construct(self):
        title = Text("Master Method", font_size=27, color=RED).to_edge(UP)
        self.add(title)
        theorem = [Tex("$T(n)$"), Tex("$T(n)\:=\:b\:.\:T(n/b)$"), Tex("$T(n)\:=\:b\:.\:T(n/b)\:+\:f(n)$"), Tex("$T(n)\:=\:a\:.\:T(n/b)\:+\:f(n)$")]
        tree = VGroup(Tex("$T(n)$", font_size=40),
                      VGroup(Tex("$T(n/b)$", font_size=35).shift(RIGHT*2.5 + DOWN*2),
                      Tex("$T(n/b)$", font_size=35).shift(LEFT*2.5 + DOWN*2)),
                      VGroup(Tex("$T(n/b^{2})$", font_size=30).shift(DOWN + LEFT*1),
                      Tex("$T(n/b^{2})$", font_size=30).shift(DOWN + LEFT*4),
                      Tex("$T(n/b^{2})$", font_size=30).shift(DOWN + RIGHT*1),
                      Tex("$T(n/b^{2})$", font_size=30).shift(DOWN + RIGHT*4)),
                      VGroup(VGroup(Dot(), Dot(), Dot()).rotate(90).scale(.25).arrange(DOWN, buff=.1),
                      VGroup(Dot(), Dot(), Dot()).rotate(90).scale(.25).arrange(DOWN, buff=.1),
                      VGroup(Dot(), Dot(), Dot()).rotate(90).scale(.25).arrange(DOWN, buff=.1),
                      VGroup(Dot(), Dot(), Dot()).rotate(90).scale(.25).arrange(DOWN, buff=.1)),
                      VGroup(Tex("$O(1)$", font_size=30),
                             Tex("$O(1)$", font_size=30),
                             Tex("$O(1)$", font_size=30),
                             Tex("$O(1)$", font_size=30))).arrange(DOWN)
        varrow = VGroup(DoubleArrow(UP, DOWN).to_edge(LEFT), Tex("$\log_{b}(n)$", font_size=35).to_edge(LEFT))
        harrow = VGroup(DoubleArrow(LEFT, RIGHT).to_edge(DOWN), Tex("$$a^{\log_{b}(n)}$$", font_size=35).to_edge(DOWN))
        b1 = BackgroundRectangle(varrow[1], color=BLACK, fill_opacity=1, buff=.3)
        b2 = BackgroundRectangle(harrow[1], color=BLACK, fill_opacity=1, buff=.3)
        l1 = always_redraw(lambda: Line(tree[0], tree[1][0], buff=.1))
        l2 = always_redraw(lambda: Line(tree[0], tree[1][1], buff=.1))
        l3 = always_redraw(lambda: Line(tree[1][0], tree[2][2], buff=.1))
        l4 = always_redraw(lambda: Line(tree[1][0], tree[2][3], buff=.1))
        l5 = always_redraw(lambda: Line(tree[1][1], tree[2][0], buff=.1))
        l6 = always_redraw(lambda: Line(tree[1][1], tree[2][1], buff=.1))
        tree[3][0].set_x(tree[2][0].get_x())
        tree[3][1].set_x(tree[2][1].get_x())
        tree[3][2].set_x(tree[2][2].get_x())
        tree[3][3].set_x(tree[2][3].get_x())
        tree[4][0].set_x(tree[2][0].get_x())
        tree[4][1].set_x(tree[2][1].get_x())
        tree[4][2].set_x(tree[2][2].get_x())
        tree[4][3].set_x(tree[2][3].get_x())
        tree1 = VGroup(Tex("$f(n)$", font_size=40).move_to(tree[0].get_center()),
                      VGroup(Tex("$f(n/b)$", font_size=35).move_to(tree[1][0].get_center()),
                      Tex("$f(n/b)$", font_size=35).move_to(tree[1][1].get_center())),
                      VGroup(Tex("$f(n/b^{2})$", font_size=30).move_to(tree[2][0].get_center()),
                      Tex("$f(n/b^{2})$", font_size=30).move_to(tree[2][1].get_center()),
                      Tex("$f(n/b^{2})$", font_size=30).move_to(tree[2][2].get_center()),
                      Tex("$f(n/b^{2})$", font_size=30).move_to(tree[2][3].get_center())))
        harrow[0].width = 10
        varrow[0].height = 6
        self.play(Write(theorem[0]))
        self.wait(1.5)
        self.play(ReplacementTransform(theorem[0], theorem[1]))
        self.wait(2)
        self.play(ReplacementTransform(theorem[1], theorem[2]))
        self.wait(2)
        self.play(ReplacementTransform(theorem[2], theorem[3]))
        self.wait(2)
        self.play(theorem[3].animate.next_to(title, DOWN))
        self.wait(1)
        self.play(Write(tree[0]))
        self.wait(1)
        self.play(Write(l1), Write(l2))
        self.play(Write(tree[1][0]), Write(tree[1][1]))
        self.wait(2)
        self.play(Write(l3), Write(l4), Write(l5), Write(l6))
        self.play(Write(tree[2][0]), Write(tree[2][1]), Write(tree[2][2]), Write(tree[2][3]))
        self.wait(2)
        self.play(Write(tree[3][0]), Write(tree[3][1]), Write(tree[3][2]), Write(tree[3][3]))
        self.wait(1)
        self.play(Write(tree[4][0]), Write(tree[4][1]), Write(tree[4][2]), Write(tree[4][3]))
        self.wait(2)
        self.play(ReplacementTransform(tree[2][0], tree1[2][0]), ReplacementTransform(tree[2][1], tree1[2][1]), ReplacementTransform(tree[2][2], tree1[2][2]), ReplacementTransform(tree[2][3], tree1[2][3]))
        self.wait(2)
        self.play(ReplacementTransform(tree[1][0], tree1[1][0]), ReplacementTransform(tree[1][1], tree1[1][1]))
        self.wait(2)
        self.play(ReplacementTransform(tree[0], tree1[0]))
        self.wait(2)
        self.play(Write(harrow[0]))
        self.wait(1)
        self.play(Write(varrow[0]))
        self.wait(2)
        self.play(Write(b1))
        self.play(Write(varrow[1]))
        self.wait(2)
        self.play(Write(b2))
        self.play(Write(harrow[1]))
        self.wait(2)
        temp = Tex("$$n^{\log_{b}(a)}$$", font_size=35).to_edge(DOWN)
        self.play(ReplacementTransform(harrow[1], temp))
        self.wait(2)
        self.play(Uncreate(harrow), Uncreate(varrow), Uncreate(b1), Uncreate(b2), Uncreate(temp))
        self.play(tree.animate.to_edge(LEFT), tree1.animate.to_edge(LEFT))
        lvl1 = Tex("$f(n)$", font_size=40).next_to(tree, RIGHT).set_y(tree[0].get_y())
        lvl2 = Tex("$a\:.\:f(n/b)$", font_size=35).next_to(tree, RIGHT).set_y(tree[1].get_y())
        lvl3 = Tex("$a^{2}\:.\:f(n/b^{2})$", font_size=30).to_edge(RIGHT).set_y(tree[2].get_y())
        lvl4 = VGroup(Tex("$a^{\log_{b}(n)}\:.\:f(n/b^{\log_{b}(n)})$", font_size=30), Tex("$n^{\log_{b}(a)}\:.\:f(n/n^{\log_{b}(b)})$", font_size=30), Tex("$n^{\log_{b}(a)}\:.\:f(n/n)$", font_size=30), Tex("$n^{\log_{b}(a)}$", font_size=30)).to_edge(RIGHT).set_y(tree[4].get_y())
        arrow1 = Arrow(lvl1.get_left(), tree[0])
        arrow2 = Arrow(lvl2.get_left(), tree[1])
        arrow3 = Arrow(lvl3.get_left(), tree[2])
        arrow4 = Arrow(lvl4.get_left(), tree[4])
        total = VGroup(Tex("Total:\:", "$f(n)\:$", "$+\:a\:.\:f(n/b)\:$", "$+\:a^{2}\:.\:f(n/b^{2})\:$", "$...\:+\:n^{\log_{b}(a)}$"), Tex("$$\sum_{i=0}^{\log_{b}n}a^{i}\:.\:f(n/b^{i})$$")).to_edge(DOWN)
        total[0][0].color = YELLOW
        total[1].next_to(total[0][0])
        self.play(Write(arrow1), reverse=True)
        self.play(Write(lvl1))
        self.wait(2)
        self.play(Write(arrow2), reverse=True)
        self.play(Write(lvl2))
        self.wait(2)
        self.play(Write(arrow3), reverse=True)
        self.play(Write(lvl3))
        self.wait(2)
        self.play(Write(arrow4), reverse=True)
        self.play(Write(lvl4[0]))
        self.wait(2)
        self.play(ReplacementTransform(lvl4[0], lvl4[1]))
        self.wait(2)
        self.play(ReplacementTransform(lvl4[1], lvl4[2]))
        self.wait(1)
        self.play(ReplacementTransform(lvl4[2], lvl4[3]))
        self.wait(1)
        self.play(Write(total[0][0]))
        self.wait(1)
        self.play(Write(total[0][1]))
        self.wait(1)
        self.play(Write(total[0][2]))
        self.wait(1)
        self.play(Write(total[0][3]))
        self.wait(1)
        self.play(Write(total[0][4]))
        self.wait(2)
        self.play(ReplacementTransform(total[0][1:], total[1]))
        self.wait(2)
        # self.add(theorem[3].next_to(title, DOWN), tree1, harrow[0], varrow[0], b1, varrow[1], b2, harrow[1], l1, l2, l3, l4, l5, l6, tree[3], tree[4])


class S9(Scene):
    def construct(self):
        title = Text("Master Method", font_size=27, color=RED).to_edge(UP)
        self.add(title)
        total = Tex("$$Total:\:\sum_{i=0}^{\log_{b}n}a^{i}\:.\:f(n/b^{i})$$", font_size=35).next_to(title, DOWN)
        wait = VGroup(Text("But Wait", color=TEAL), Text("remember when we said we needn't be specific", color=DARK_BLUE), Text("we only need the biggest factor", color=BLUE))
        self.play(Write(wait[0]))
        self.wait(1)
        self.play(ReplacementTransform(wait[0], wait[1]))
        self.wait(2)
        self.play(ReplacementTransform(wait[1], wait[2]))
        self.wait(2)
        self.play(Unwrite(wait[2]), Write(total))
        self.wait(2)
        subtitle = Text("we have three cases", font_size=27, color=PURPLE).set_y(1)
        cases = VGroup(Tex("1.\:the problem gets easier $\Longrightarrow$\:", "the root is the hardest", font_size=35),
                       Tex("2.\:the problem gets harder $\Longrightarrow$\:", "the leaves are the hardest", font_size=35),
                       Tex("3.\:the problem levels equally hard $\Longrightarrow$\:", "all levels are important", font_size=35)).arrange(DOWN, buff=.6)
        cases[0].set_y(0)
        cases[1].set_y(-1.5)
        cases[2].set_y(-3)
        casemath = VGroup(Tex("$T(n)\:=\:O(work\:in\:the\:root)$", "$T(n)\:=\:O(f(n))$", font_size=35),
                          Tex("$T(n)\:=\:O(leaves\:work)$", "$T(n)\:=\:O(n^{\log_{b}(a)})$", font_size=35),
                          Tex( "$T(n)\:=\:height\:.\:O(any\:level)$", "$T(n)\:=\:\log_{b}(n)\:.\:O(n^{\log_{b}(a)})$", font_size=35))
        for i in range(len(casemath)):
            for j in range(len(casemath[i])):
                casemath[i][j].next_to(cases[i][0])
        self.play(Write(subtitle))
        self.wait(1)
        for i in range(len(cases)):
            self.play(Write(cases[i][0]))
            self.wait(1)
            self.play(Write(cases[i][1]))
            self.wait(1)
            self.play(ReplacementTransform(cases[i][1], casemath[i][0]))
            self.wait(2)
            self.play(ReplacementTransform(casemath[i][0], casemath[i][1]))
            self.wait(2)
        mathtitle = Text("mathematical representation", font_size=25, color=ORANGE).next_to(title, DOWN)
        self.play(ReplacementTransform(total, mathtitle))
        self.wait(1)
        theorem = Tex("$for\:T(n)\:=\:a\:.\:T(n/b)+O(n^{d})\:\:if\:\:a\geq1,\:b>1,\:d\geq0$", color=YELLOW, font_size=40).set_y(1)
        mathcases = VGroup(Tex("$1.\:\:if\:d\:>\:\log_{b}(a)\:\:\:$", "then\:$T(n)\:=\:O(n^{d})$", font_size=35),
                           Tex("$2.\:\:if\:d\:<\:\log_{b}(a)\:\:\:$", "then\:$T(n)\:=\:O(n^{\log_{b}(a)})$", font_size=35),
                           Tex("$3.\:\:if\:d\:=\:\log_{b}(a)\:\:\:$", "then\:$T(n)\:=\:O(n^{d}\:\log_{b}(n))$", font_size=35))
        mathcases[0].set_y(0).color = RED
        mathcases[1].set_y(-1.5).color = GREEN
        mathcases[2].set_y(-3).color = BLUE
        self.play(ReplacementTransform(subtitle, theorem))
        self.wait(4)
        for i in range(len(cases)):
            self.play(ReplacementTransform(VGroup(cases[i], casemath[i]), mathcases[i]))
            self.wait(4)
        self.play(Unwrite(mathcases), Unwrite(mathtitle), Unwrite(theorem))
        self.wait(1)
        tree = Text("Tree Method", font_size=27, color=GREEN).to_edge(UP)
        self.play(ReplacementTransform(title, tree))


class S10(Scene):
    def construct(self):
        title = Text("Tree Method", font_size=27, color=GREEN).to_edge(UP)
        self.add(title)
        subtitle = VGroup(Text("master method doesn't cover all cases", font_size=27, color=TEAL),
                          Text("it has dependency over the fact that the branching is symmetrical", font_size=27, color=TEAL),
                          Text("splitting this function we get non symmetrical recursive calls", font_size=27, color=TEAL),
                          Text("which renders the master method useless", font_size=27, color=TEAL),
                          Text("try to  get sum of work at each level", font_size=27, color=TEAL),
                          Text("usually in any symmetrical tree all leaves are at the last level", font_size=27, color=TEAL),
                          Text("but here we have to compute the best and worst case to find the complexity", font_size=27, color=TEAL)).set_y(2.25)
        problem = VGroup(Tex("$T(n)\:=\:T(n/2)\:+\:2\:T(n/4)\:+\:O(n)$"),
                         Tex("$T(n/2)\:=\:T(n/4)\:+\:2\:T(n/8)\:+\:O(n/2)$"),
                         Tex("$T(n/4)\:=\:T(n/8)\:+\:2\:T(n/16)\:+\:O(n/4)$"),
                         Tex("$T(n)\:=\:sum\:of\:work\:at\:all\:levels$"),).set_y(1)
        tree = VGroup(Tex("T(n)", font_size=30).set_y(1),
                      VGroup(Tex("T(n/2)", font_size=30), Tex("T(n/4)", font_size=30), Tex("T(n/4)", font_size=30)).set_y(0),
                      VGroup(Tex("T(n/4)", font_size=30), Tex("T(n/8)", font_size=30), Tex("T(n/8)", font_size=30), Tex("T(n/8)", font_size=30), Tex("T(n/16)", font_size=30), Tex("T(n/16)", font_size=30), Tex("T(n/8)", font_size=30), Tex("T(n/16)", font_size=30), Tex("T(n/16)", font_size=30)).set_y(-1),
                      VGroup(Dot(), Dot(), Dot()).rotate(90).scale(.25).arrange(DOWN, buff=.1), Tex("O(1)", font_size=30)).set_y(-1)
        tree[3].next_to(tree[2], DOWN)
        tree[4].next_to(tree[3], DOWN)
        tree[1][0].set_x(-4.5)
        tree[1][1].set_x(0)
        tree[1][2].set_x(4.5)
        tree[2][0].set_x(-6)
        tree[2][1].set_x(-4.5)
        tree[2][2].set_x(-3)
        tree[2][3].set_x(-1.5)
        tree[2][4].set_x(0)
        tree[2][5].set_x(1.5)
        tree[2][6].set_x(3)
        tree[2][7].set_x(4.5)
        tree[2][8].set_x(6)
        lines = VGroup(Line(tree[0].get_left(), tree[1][0].get_right(), buff=.1),
                       Line(tree[0].get_bottom(), tree[1][1].get_top(), buff=.1),
                       Line(tree[0].get_right(), tree[1][2].get_left(), buff=.1),
                       Line(tree[1][0], tree[2][0], buff=.1),
                       always_redraw(lambda: Line(tree[1][0].get_bottom(), tree[2][1].get_top(), buff=.1)),
                       Line(tree[1][0], tree[2][2], buff=.1),
                       Line(tree[1][1], tree[2][3], buff=.1),
                       always_redraw(lambda: Line(tree[1][1].get_bottom(), tree[2][4].get_top(), buff=.1)),
                       Line(tree[1][1], tree[2][5], buff=.1),
                       Line(tree[1][2], tree[2][6], buff=.1),
                       always_redraw(lambda: Line(tree[1][2].get_bottom(), tree[2][7].get_top(), buff=.1)),
                       Line(tree[1][2], tree[2][8], buff=.1))
        transtree = VGroup(Tex("O(n)", font_size=30).move_to(tree[0].get_center()),
                           Tex("O(n/2)", font_size=30).move_to(tree[1][0].get_center()),
                           Tex("O(n/4)", font_size=30).move_to(tree[1][1].get_center()),
                           Tex("O(n/4)", font_size=30).move_to(tree[1][2].get_center()),
                           Tex("O(n/4)", font_size=30).move_to(tree[2][0].get_center()),
                           Tex("O(n/8)", font_size=30).move_to(tree[2][1].get_center()),
                           Tex("O(n/8)", font_size=30).move_to(tree[2][2].get_center()),
                           Tex("O(n/8)", font_size=30).move_to(tree[2][3].get_center()),
                           Tex("O(n/16)", font_size=30).move_to(tree[2][4].get_center()),
                           Tex("O(n/16)", font_size=30).move_to(tree[2][5].get_center()),
                           Tex("O(n/8)", font_size=30).move_to(tree[2][6].get_center()),
                           Tex("O(n/16)", font_size=30).move_to(tree[2][7].get_center()),
                           Tex("O(n/16)", font_size=30).move_to(tree[2][8].get_center()))
        newtree = VGroup(Tex("O(n)", font_size=30).move_to(tree[0].get_center()),
                         Tex("O(n/2)", font_size=30).move_to(tree[1][0].get_center()),
                         Tex("O(n/4)", font_size=30).move_to(tree[1][1].get_center()),
                         Tex("O(n/4)", font_size=30).move_to(tree[1][2].get_center()),
                         Tex("O(n/4)", font_size=30).move_to(tree[2][0].get_center()),
                         Tex("O(n/8)", font_size=30).move_to(tree[2][1].get_center()),
                         Tex("O(n/8)", font_size=30).move_to(tree[2][2].get_center()),
                         Tex("O(n/8)", font_size=30).move_to(tree[2][3].get_center()),
                         Tex("O(n/16)", font_size=30).move_to(tree[2][4].get_center()),
                         Tex("O(n/16)", font_size=30).move_to(tree[2][5].get_center()),
                         Tex("O(n/8)", font_size=30).move_to(tree[2][6].get_center()),
                         Tex("O(n/16)", font_size=30).move_to(tree[2][7].get_center()),
                         Tex("O(n/16)", font_size=30).move_to(tree[2][8].get_center()))
        newlines = VGroup(always_redraw(lambda: Line(newtree[0].get_left(), newtree[1].get_right(), buff=.1)),
                          always_redraw(lambda: Line(newtree[0].get_bottom(), newtree[2].get_top(), buff=.1)),
                          always_redraw(lambda: Line(newtree[0].get_right(), newtree[3].get_left(), buff=.1)),
                          always_redraw(lambda: Line(newtree[1], newtree[4], buff=.1)),
                          always_redraw(lambda: Line(newtree[1].get_bottom(), newtree[5].get_top(), buff=.1)),
                          always_redraw(lambda: Line(newtree[1], newtree[6], buff=.1)),
                          always_redraw(lambda: Line(newtree[2], newtree[7], buff=.1)),
                          always_redraw(lambda: Line(newtree[2].get_bottom(), newtree[8].get_top(), buff=.1)),
                          always_redraw(lambda: Line(newtree[2], newtree[9], buff=.1)),
                          always_redraw(lambda: Line(newtree[3], newtree[10], buff=.1)),
                          always_redraw(lambda: Line(newtree[3].get_bottom(), newtree[11].get_top(), buff=.1)),
                          always_redraw(lambda: Line(newtree[3], newtree[12], buff=.1)))

        sumtree = VGroup(Tex("O(n)", font_size=30).move_to(tree[1][1].get_center()),
                         Tex("O(n)", font_size=30).move_to(tree[2][4].get_center()),
                         Tex("O(n)", font_size=30).move_to(tree[4].get_center()),
                         Tex("right ?", font_size=30).move_to(tree[4].get_center()))
        self.play(Write(subtitle[0]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[0], subtitle[1]))
        self.wait(3)
        self.play(ReplacementTransform(subtitle[1], subtitle[2]))
        self.wait(3)
        self.play(Write(problem[0]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[2], subtitle[3]))
        self.wait(2)
        self.play(Write(tree[0]))
        self.wait(1)
        self.play(Write(lines[0]), Write(lines[1]), Write(lines[2]))
        self.play(ReplacementTransform(tree[0], transtree[0]))
        self.wait(1)
        self.play(Write(tree[1][0]), Write(tree[1][1]), Write(tree[1][2]))
        self.wait(2)
        self.play(ReplacementTransform(problem[0], problem[1]))
        self.wait(2)
        self.play(Write(lines[3]), Write(lines[4]), Write(lines[5]))
        self.play(ReplacementTransform(tree[1][0], transtree[1]))
        self.wait(1)
        self.play(Write(tree[2][0]), Write(tree[2][1]), Write(tree[2][2]))
        self.wait(2)
        self.play(ReplacementTransform(problem[1], problem[2]))
        self.wait(2)
        self.play(Write(lines[6]), Write(lines[7]), Write(lines[8]))
        self.play(ReplacementTransform(tree[1][1], transtree[2]))
        self.wait(1)
        self.play(Write(tree[2][3]), Write(tree[2][4]), Write(tree[2][5]))
        self.wait(2)
        self.play(Write(lines[9]), Write(lines[10]), Write(lines[11]))
        self.play(ReplacementTransform(tree[1][2], transtree[3]))
        self.wait(1)
        self.play(Write(tree[2][6]), Write(tree[2][7]), Write(tree[2][8]))
        self.wait(2)
        self.play(Write(tree[3]))
        self.wait(1)
        self.play(ReplacementTransform(tree[2][0], transtree[4]), ReplacementTransform(tree[2][1], transtree[5]), ReplacementTransform(tree[2][2], transtree[6]), ReplacementTransform(tree[2][3], transtree[7]), ReplacementTransform(tree[2][4], transtree[8]), ReplacementTransform(tree[2][5], transtree[9]), ReplacementTransform(tree[2][6], transtree[10]), ReplacementTransform(tree[2][7], transtree[11]), ReplacementTransform(tree[2][8], transtree[12]))
        self.wait(2)
        self.play(Write(tree[4]))
        self.wait(2)
        self.play(ReplacementTransform(problem[2], problem[3]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[3], subtitle[4]))
        self.wait(1)
        self.play(Unwrite(lines[0]), Unwrite(lines[2]))
        self.wait(1)
        self.play(ReplacementTransform(transtree[1:4], sumtree[0]))
        self.wait(1)
        self.play(Unwrite(lines[3:7]), Unwrite(lines[8:]))
        self.wait(1)
        self.play(ReplacementTransform(transtree[4:], sumtree[1]))
        self.wait(1)
        self.play(ReplacementTransform(tree[4], sumtree[2]))
        self.wait(1)
        self.play(ReplacementTransform(sumtree[2], sumtree[3]))
        self.wait(1)
        self.play(ReplacementTransform(subtitle[4], subtitle[5]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[5], subtitle[6]))
        self.wait(2)
        self.play(Unwrite(sumtree[3]))
        self.play(Write(newlines[0]), Write(newlines[2]))
        self.play(ReplacementTransform(sumtree[0], newtree[2]), Write(newtree[1]), Write(newtree[3]), ReplacementTransform(transtree[0], newtree[0]))
        self.play(Write(newlines[3:7]), Write(newlines[8:]))
        self.play(ReplacementTransform(sumtree[1], newtree[8]), Write(newtree[4:8]), Write(newtree[9:]))
        self.wait(2)
        leftist = Tex("$O(n/2^{i})$", font_size=30).next_to(tree[3], DOWN).set_x(-6.5)
        middelist = Tex("$O(n/4^{i})$", font_size=30).next_to(tree[3], DOWN)
        rightist = Tex("$O(n/4^{i}$)", font_size=30).next_to(tree[3], DOWN).set_x(6.5)
        leftdot = VGroup(Dot(), Dot(), Dot()).scale(.25).arrange(DOWN, buff=.1).next_to(tree[3])
        leftdot[0].set_x(-6)
        leftdot[1].set_x(-6.1)
        leftdot[2].set_x(-6.2)
        rightdot = VGroup(Dot(), Dot(), Dot()).scale(.25).arrange(DOWN, buff=.1).next_to(tree[3]).set_x(6.5)
        rightdot[0].set_x(6)
        rightdot[1].set_x(6.1)
        rightdot[2].set_x(6.2)
        complexity = VGroup(Tex("$n/4^{i}\:=\:1$"),
                            Tex("$n\:=\:4^{i}$"),
                            Tex("$\log_{4}(n)\:=\:\log_{4}(4^{i})$"),
                            Tex("$\log_{4}(n)\:=\:i$"),
                            Tex("best case height = $\log_{4}(n)$"),
                            Tex("best case complexity = $n\:\log_{4}(n)$"),
                            Tex("$n/2^{i}\:=\:1$"),
                            Tex("$n\:=\:2^{i}$"),
                            Tex("$\log_{2}(n)\:=\:\log_{2}(2^{i})$"),
                            Tex("$\log_{2}(n)\:=\:i$"),
                            Tex("worst case height = $\log_{2}(n)$"),
                            Tex("worst case complexity = $n\:\log_{2}(n)$"),
                            Tex("$n\:\log_{2}(n)\:\geq\:complexity\:\geq\:n\:\log_{4}(n)$"),
                            Tex("complexity = $n\:\log(n)$")).set_y(1)
        self.play(Write(rightdot))
        self.play(Write(rightist), Write(middelist))
        self.wait(1)
        self.play(ReplacementTransform(problem[3], complexity[0]))
        self.wait(1)
        for i in range(5):
            self.play(ReplacementTransform(complexity[i], complexity[i+1]))
            self.wait(2)
        self.play(Write(leftdot))
        self.play(Write(leftist))
        self.wait(2)
        for i in range(5, len(complexity)-1):
            self.play(ReplacementTransform(complexity[i], complexity[i + 1]))
            self.wait(1)


class S11(Scene):
    def construct(self):
        title = Text("Substitution Method", font_size=27, color=BLUE).to_edge(UP)
        self.add(title)
        subtitle = VGroup(Text("tree method can be an overkill when dealing with non-splitting recurrence", font_size=25, color=GREEN),
                          Text("substitution method uses an algorithm called plug and chug", font_size=25, color=GREEN),
                          Text("which is different from the usual divide and conquer", font_size=25, color=GREEN),
                          Text("uses mathematical induction to find a formula that returns the cumulative complexity at a level", font_size=25, color=GREEN),
                          Text("to find the total complexity we have to substitute with the last level in this formula", font_size=25, color=GREEN),
                          Text("now substitute n with every i in the formula", font_size=25, color=GREEN)).set_y(2.25)
        problem = VGroup(Tex("$T(n)\:=\:2\:T(n-1)\:+\:1$"),
                         Tex("$T(n)\:=\:2\:[\:$", "$2\:T(n-2):+\:1$", "$\:]\:+\:1$"),
                         Tex("$T(n)\:=\:2\:*\:2\:T(n-2)\:+\:2\:+\:1$"),
                         Tex("$T(n)\:=\:2^{2}\:T(n-2)\:+\:1\:+\:2$"),
                         Tex("$T(n)\:=\:2^{2}\:[\:$", "$2\:T(n-3):+\:1$", "$\:]\:+\:1\:+\:2$"),
                         Tex("$T(n)\:=\:2^{2}\:*\:2\:T(n-3)\:+\:2^{2}\:+\:2\:+\:1$"),
                         Tex("$T(n)\:=\:2^{3}\:T(n-3)\:+\:2^{2}\:+\:2\:+\:1$"),
                         Tex("$$T(n)\:=\:2^{i}\:T(n-i)\:+\:\sum_{j=0}^{i-1}2^{j}$$"),
                         Tex("$$T(n)\:=\:2^{n}\:T(n-n)\:+\:\sum_{j=0}^{n-1}2^{j}$$"),
                         Tex("$$T(n)\:=\:2^{n}\:+\:\sum_{j=0}^{n-1}2^{j}$$"),
                         Tex("$$T(n)\:=\:\sum_{j=0}^{n}2^{j}$$"),
                         Tex("$T(n)\:=\:2^{n}\:-\:1$"),).set_y(1)
        proof = VGroup(Tex("$T(n-1)\:=\:$", "$2\:T(n-2)\:+\:1$"),
                       Tex("$T(n-2)\:=\:$", "$2\:T(n-3)\:+\:1$"),
                       Tex("recursion ends when", "$\:n\:-\:i\:=\:0$"),
                       Tex("$\:n\:=\:i$"),
                       Tex(r"$\because$\:this is a geometric series, and\:$a\:=\:1,\:r\:=\:2$"),
                       Tex(r"$$\therefore\:\sum_{j=0}^{n}2^{j}\:=\:\frac{2^{n}\:-\:1}{2-1}$$")).set_y(-1)
        proof[3].next_to(proof[2][0])
        self.play(Write(subtitle[0]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[0], subtitle[1]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[1], subtitle[2]))
        self.wait(1)
        self.play(Write(problem[0]))
        self.wait(1)
        self.play(Write(proof[0]))
        self.wait(2)
        self.play(ReplacementTransform(problem[0], VGroup(problem[1][0], problem[1][2])))
        self.wait(1)
        self.play(proof[0][1].animate.move_to(problem[1][1].get_center()))
        self.wait(2)
        self.play(ReplacementTransform(VGroup(problem[1], proof[0][1]), problem[2]))
        self.wait(2)
        self.play(ReplacementTransform(problem[2], problem[3]))
        self.wait(2)
        self.play(ReplacementTransform(proof[0][0], proof[1]))
        self.wait(2)
        self.play(ReplacementTransform(problem[3], VGroup(problem[4][0], problem[4][2])))
        self.wait(1)
        self.play(proof[1][1].animate.move_to(problem[4][1].get_center()))
        self.wait(2)
        self.play(ReplacementTransform(VGroup(problem[4], proof[1][1]), problem[5]))
        self.wait(2)
        self.play(ReplacementTransform(problem[5], problem[6]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[2], subtitle[3]))
        self.wait(2)
        self.play(ReplacementTransform(problem[6], problem[7]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[3], subtitle[4]))
        self.wait(2)
        self.play(ReplacementTransform(proof[1][0], proof[2]))
        self.wait(2)
        self.play(ReplacementTransform(proof[2][1], proof[3]))
        self.wait(2)
        self.play(ReplacementTransform(subtitle[4], subtitle[5]))
        self.wait(2)
        self.play(ReplacementTransform(problem[7], problem[8]))
        self.wait(2)
        self.play(ReplacementTransform(problem[8], problem[9]))
        self.wait(2)
        self.play(ReplacementTransform(problem[9], problem[10]))
        self.wait(2)
        self.play(ReplacementTransform(VGroup(proof[2][0], proof[3]), proof[4]))
        self.wait(2)
        self.play(ReplacementTransform(proof[4], proof[5]))
        self.wait(2)
        self.play(ReplacementTransform(problem[10], problem[11]))
        self.wait(2)


class Outro(Scene):
    def construct(self):
        outro = Tex("this was", " Algorithms analysis and design")
        outro[0].set_color(GREEN)
        outro[1].set_color(RED)
        t = Text("With Osama Khalifa", color=BLUE, font_size=35)
        self.play(Write(VGroup(outro, t).arrange(DOWN)), run_time=5)
        # self.add(VGroup(outro, t).arrange(DOWN))
