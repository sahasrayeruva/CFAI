import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from graph import CampusGraph
from search import SearchAlgorithms
from explain import RouteExplainer


class CampusNavigationGUI:

    def __init__(self, root):

        self.root = root
        self.root.title(
            "Intelligent Campus Navigation Assistant"
        )

        self.root.geometry("900x650")

        self.graph = CampusGraph("campus_map.json")

        self.search = SearchAlgorithms(self.graph)

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Intelligent Campus Navigation Assistant",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Source").grid(row=0, column=0)

        self.source = ttk.Combobox(
            frame,
            values=self.graph.nodes(),
            width=30
        )
        self.source.grid(row=0, column=1)

        tk.Label(frame, text="Destination").grid(row=1, column=0)

        self.destination = ttk.Combobox(
            frame,
            values=self.graph.nodes(),
            width=30
        )
        self.destination.grid(row=1, column=1)

        algo_frame = tk.LabelFrame(
            self.root,
            text="Algorithm"
        )

        algo_frame.pack(fill="x", padx=20)

        self.algorithm = tk.StringVar(value="astar")

        algorithms = [
            ("BFS", "bfs"),
            ("DFS", "dfs"),
            ("UCS", "ucs"),
            ("Greedy", "greedy"),
            ("A*", "astar")
        ]

        for text, value in algorithms:
            tk.Radiobutton(
                algo_frame,
                text=text,
                variable=self.algorithm,
                value=value
            ).pack(anchor="w")

        constraint_frame = tk.LabelFrame(
            self.root,
            text="Constraints"
        )

        constraint_frame.pack(fill="x", padx=20, pady=10)

        self.avoid_construction = tk.BooleanVar()
        self.avoid_crowds = tk.BooleanVar()
        self.accessible = tk.BooleanVar()

        tk.Checkbutton(
            constraint_frame,
            text="Avoid Construction",
            variable=self.avoid_construction
        ).pack(anchor="w")

        tk.Checkbutton(
            constraint_frame,
            text="Avoid Crowds",
            variable=self.avoid_crowds
        ).pack(anchor="w")

        tk.Checkbutton(
            constraint_frame,
            text="Wheelchair Accessible",
            variable=self.accessible
        ).pack(anchor="w")

        tk.Button(
            self.root,
            text="Find Route",
            command=self.find_route,
            bg="green",
            fg="white",
            font=("Arial", 12, "bold")
        ).pack(pady=15)

        self.output = tk.Text(
            self.root,
            height=18,
            width=100
        )

        self.output.pack(padx=10, pady=10)

    def find_route(self):

        source = self.source.get()
        destination = self.destination.get()

        if not source or not destination:

            messagebox.showerror(
                "Error",
                "Select source and destination"
            )

            return

        algo = self.algorithm.get()

        try:

            if algo == "bfs":
                 result = self.search.bfs(source, destination)
            elif algo == "dfs":
                 result = self.search.dfs(source, destination)
            elif algo == "ucs":
                 result = self.search.ucs(source, destination)
            elif algo == "greedy":
                 result = self.search.greedy(source, destination)
            else:
                 result = self.search.astar(source, destination)
            path = result.path
            cost = result.cost

            constraints = []

            if self.avoid_construction.get():
                constraints.append(
                    "Construction Areas Avoided"
                )

            if self.avoid_crowds.get():
                constraints.append(
                    "Crowded Areas Avoided"
                )

            if self.accessible.get():
                constraints.append(
                    "Wheelchair Accessible Route"
                )

            explanation = RouteExplainer.generate_explanation(
                path=path,
                distance=cost,
                algorithm=algo,
                constraints=constraints
            )

            self.output.delete(
                "1.0",
                tk.END
            )

            self.output.insert(
                tk.END,
                explanation
            )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                str(e)
            )


if __name__ == "__main__":

    root = tk.Tk()

    app = CampusNavigationGUI(root)

    root.mainloop()