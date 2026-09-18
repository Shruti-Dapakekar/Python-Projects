import tkinter as tk
from tkinter import font
import random

# ============================================================
# SNAKE • WATER • GUN
# ============================================================

# Game values
# Snake = 1
# Water = -1
# Gun = 0

CHOICES = {
    "Snake": 1,
    "Water": -1,
    "Gun": 0
}

NAMES = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

ICONS = {
    1: "🐍",
    -1: "💧",
    0: "🔫"
}


class SnakeWaterGun:

    def __init__(self, root):

        self.root = root

        self.root.title("Snake Water Gun")
        self.root.geometry("1100x760")
        self.root.minsize(850, 650)
        self.root.configure(bg="#07111f")

        # Score
        self.user_score = 0
        self.computer_score = 0

        # Prevent clicking multiple times during animation
        self.round_active = False

        self.animation_ids = []

        # Fonts
        self.title_font = font.Font(
            family="Segoe UI",
            size=30,
            weight="bold"
        )

        self.subtitle_font = font.Font(
            family="Segoe UI",
            size=12
        )

        self.heading_font = font.Font(
            family="Segoe UI",
            size=19,
            weight="bold"
        )

        self.choice_font = font.Font(
            family="Segoe UI Emoji",
            size=52
        )

        self.name_font = font.Font(
            family="Segoe UI",
            size=15,
            weight="bold"
        )

        self.result_font = font.Font(
            family="Segoe UI",
            size=24,
            weight="bold"
        )

        self.button_font = font.Font(
            family="Segoe UI",
            size=14,
            weight="bold"
        )

        self.build_ui()

        self.reset_round()

    # ========================================================
    # BUILD UI
    # ========================================================

    def build_ui(self):

        main = tk.Frame(
            self.root,
            bg="#07111f"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=25
        )

        # ---------------- HEADER ----------------

        tk.Label(
            main,
            text="SNAKE  •  WATER  •  GUN",
            bg="#07111f",
            fg="#f5f7ff",
            font=self.title_font
        ).pack()

        tk.Label(
            main,
            text="THINK  •  CHOOSE  •  PLAY  •  WIN!",
            bg="#07111f",
            fg="#9aa9bd",
            font=self.subtitle_font
        ).pack(pady=(2, 18))

        # ---------------- BATTLE AREA ----------------

        battle = tk.Frame(
            main,
            bg="#07111f"
        )

        battle.pack(
            fill="x"
        )

        # YOU card

        self.create_player_card(
            battle,
            "YOU",
            "#48e889",
            True
        )

        # VS

        vs_frame = tk.Frame(
            battle,
            bg="#07111f",
            width=90
        )

        vs_frame.pack(
            side="left",
            fill="y"
        )

        vs_frame.pack_propagate(False)

        self.vs_label = tk.Label(
            vs_frame,
            text="VS",
            bg="#07111f",
            fg="#ffd166",
            font=font.Font(
                family="Segoe UI",
                size=27,
                weight="bold"
            )
        )

        self.vs_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # COMPUTER card

        self.create_player_card(
            battle,
            "COMPUTER",
            "#ff5f87",
            False
        )

        # ---------------- RESULT ----------------

        self.result_frame = tk.Frame(
            main,
            bg="#10243a",
            highlightthickness=2,
            highlightbackground="#8b5cf6"
        )

        self.result_frame.pack(
            fill="x",
            pady=16,
            ipady=12
        )

        self.result_label = tk.Label(
            self.result_frame,
            text="Choose your weapon!",
            bg="#10243a",
            fg="#f5f7ff",
            font=self.result_font
        )

        self.result_label.pack()

        self.detail_label = tk.Label(
            self.result_frame,
            text="",
            bg="#10243a",
            fg="#9aa9bd",
            font=self.subtitle_font
        )

        self.detail_label.pack(
            pady=(4, 0)
        )

        # ---------------- SCORE ----------------

        score_frame = tk.Frame(
            main,
            bg="#07111f"
        )

        score_frame.pack(
            fill="x",
            pady=(0, 12)
        )

        self.user_score_label = tk.Label(
            score_frame,
            text="YOU\n0",
            bg="#07111f",
            fg="#48e889",
            font=font.Font(
                family="Segoe UI",
                size=16,
                weight="bold"
            )
        )

        self.user_score_label.pack(
            side="left",
            expand=True
        )

        self.round_label = tk.Label(
            score_frame,
            text="ROUND 1",
            bg="#07111f",
            fg="#9aa9bd",
            font=self.subtitle_font
        )

        self.round_label.pack(
            side="left",
            expand=True
        )

        self.computer_score_label = tk.Label(
            score_frame,
            text="COMPUTER\n0",
            bg="#07111f",
            fg="#ff5f87",
            font=font.Font(
                family="Segoe UI",
                size=16,
                weight="bold"
            )
        )

        self.computer_score_label.pack(
            side="left",
            expand=True
        )

        # ---------------- WEAPON TITLE ----------------

        tk.Label(
            main,
            text="CHOOSE YOUR WEAPON",
            bg="#07111f",
            fg="#f5f7ff",
            font=self.heading_font
        ).pack(
            pady=(0, 10)
        )

        # ---------------- WEAPON BUTTONS ----------------

        buttons_frame = tk.Frame(
            main,
            bg="#07111f"
        )

        buttons_frame.pack(
            fill="x"
        )

        self.choice_buttons = {}

        choices = [
            ("Snake", "🐍", "#48e889"),
            ("Water", "💧", "#4dc7ff"),
            ("Gun", "🔫", "#ff5f87")
        ]

        for name, icon, accent in choices:

            button = self.create_choice_button(
                buttons_frame,
                name,
                icon,
                accent
            )

            button.pack(
                side="left",
                fill="both",
                expand=True,
                padx=7
            )

            self.choice_buttons[name] = button

        # ---------------- PLAY AGAIN ----------------

        self.play_again_button = tk.Button(
            main,
            text="↻   PLAY AGAIN",
            command=self.reset_round,
            bg="#8b5cf6",
            fg="white",
            activebackground="#a78bfa",
            activeforeground="white",
            font=self.button_font,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=35,
            pady=11
        )

        self.play_again_button.pack(
            pady=18
        )

        self.add_button_hover(
            self.play_again_button,
            "#8b5cf6",
            "#a78bfa"
        )

        # ---------------- RULES ----------------

        tk.Label(
            main,
            text="🐍 Snake beats Water    •    💧 Water beats Gun    •    🔫 Gun beats Snake",
            bg="#07111f",
            fg="#74859b",
            font=font.Font(
                family="Segoe UI",
                size=10
            )
        ).pack()

    # ========================================================
    # PLAYER CARD
    # ========================================================

    def create_player_card(
        self,
        parent,
        title,
        accent,
        is_user
    ):

        card = tk.Frame(
            parent,
            bg="#0d1b2e",
            highlightthickness=2,
            highlightbackground=accent
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            card,
            text=title,
            bg="#0d1b2e",
            fg="#f5f7ff",
            font=self.heading_font
        ).pack(
            pady=(13, 0)
        )

        icon = tk.Label(
            card,
            text="❔",
            bg="#0d1b2e",
            fg=accent,
            font=self.choice_font
        )

        icon.pack(
            pady=2
        )

        name = tk.Label(
            card,
            text="Waiting...",
            bg="#0d1b2e",
            fg="#f5f7ff",
            font=self.name_font
        )

        name.pack(
            pady=(0, 13)
        )

        if is_user:

            self.user_icon = icon
            self.user_choice_label = name

        else:

            self.computer_icon = icon
            self.computer_choice_label = name

    # ========================================================
    # CHOICE BUTTON
    # ========================================================

    def create_choice_button(
        self,
        parent,
        name,
        icon,
        accent
    ):

        frame = tk.Frame(
            parent,
            bg="#10243a",
            highlightthickness=2,
            highlightbackground=accent,
            cursor="hand2"
        )

        icon_label = tk.Label(
            frame,
            text=icon,
            bg="#10243a",
            fg="#f5f7ff",
            font=font.Font(
                family="Segoe UI Emoji",
                size=34
            ),
            cursor="hand2"
        )

        icon_label.pack(
            pady=(12, 1)
        )

        text_label = tk.Label(
            frame,
            text=name,
            bg="#10243a",
            fg="#f5f7ff",
            font=self.button_font,
            cursor="hand2"
        )

        text_label.pack(
            pady=(0, 12)
        )

        widgets = (
            frame,
            icon_label,
            text_label
        )

        for widget in widgets:

            widget.bind(
                "<Button-1>",
                lambda event, n=name:
                self.play(n)
            )

            widget.bind(
                "<Enter>",
                lambda event,
                f=frame,
                i=icon_label,
                t=text_label,
                c=accent:
                self.choice_hover(
                    f,
                    i,
                    t,
                    c,
                    True
                )
            )

            widget.bind(
                "<Leave>",
                lambda event,
                f=frame,
                i=icon_label,
                t=text_label,
                c=accent:
                self.choice_hover(
                    f,
                    i,
                    t,
                    c,
                    False
                )
            )

        frame.icon_label = icon_label
        frame.text_label = text_label
        frame.accent = accent

        return frame

    # ========================================================
    # HOVER EFFECT
    # ========================================================

    def choice_hover(
        self,
        frame,
        icon_label,
        text_label,
        accent,
        active
    ):

        if active:
            bg = accent
        else:
            bg = "#10243a"

        frame.configure(
            bg=bg
        )

        icon_label.configure(
            bg=bg
        )

        text_label.configure(
            bg=bg
        )

    def add_button_hover(
        self,
        button,
        normal,
        hover
    ):

        button.bind(
            "<Enter>",
            lambda event:
            button.configure(bg=hover)
        )

        button.bind(
            "<Leave>",
            lambda event:
            button.configure(bg=normal)
        )

    # ========================================================
    # PLAY
    # ========================================================

    def play(self, choice_name):

        if self.round_active:
            return

        self.round_active = True

        self.clear_animation()

        # User choice
        you = CHOICES[choice_name]

        # Computer choice
        computer = random.choice(
            [-1, 0, 1]
        )

        # Show user's choice

        self.user_icon.configure(
            text=ICONS[you]
        )

        self.user_choice_label.configure(
            text=NAMES[you]
        )

        # Computer animation

        self.computer_icon.configure(
            text="❔"
        )

        self.computer_choice_label.configure(
            text="Thinking..."
        )

        self.result_label.configure(
            text="⚔  BATTLE STARTING...",
            fg="#ffd166"
        )

        self.detail_label.configure(
            text="Computer is choosing..."
        )

        self.animate_computer(
            you,
            computer,
            0
        )

    # ========================================================
    # COMPUTER ANIMATION
    # ========================================================

    def animate_computer(
        self,
        you,
        computer,
        step
    ):

        if step < 9:

            values = [-1, 0, 1]

            value = values[
                step % 3
            ]

            self.computer_icon.configure(
                text=ICONS[value]
            )

            self.computer_choice_label.configure(
                text=NAMES[value]
            )

            if step % 2 == 0:

                self.vs_label.configure(
                    text="VS"
                )

            else:

                self.vs_label.configure(
                    text="⚡"
                )

            delay = 80 + step * 15

            animation_id = self.root.after(
                delay,
                lambda:
                self.animate_computer(
                    you,
                    computer,
                    step + 1
                )
            )

            self.animation_ids.append(
                animation_id
            )

        else:

            self.computer_icon.configure(
                text=ICONS[computer]
            )

            self.computer_choice_label.configure(
                text=NAMES[computer]
            )

            self.vs_label.configure(
                text="VS"
            )

            self.show_result(
                you,
                computer
            )

    # ========================================================
    # RESULT
    # ========================================================

    def show_result(
        self,
        you,
        computer
    ):

        # DRAW

        if computer == you:

            result = "IT'S A DRAW!"

            color = "#ffd166"

            detail = (
                f"Both chose {NAMES[you]}!"
            )

        # USER WINS

        elif (
            (you == 1 and computer == -1)
            or
            (you == -1 and computer == 0)
            or
            (you == 0 and computer == 1)
        ):

            result = "🎉 YOU WIN!"

            color = "#48e889"

            if you == 1:

                detail = "🐍 Snake beats Water!"

            elif you == -1:

                detail = "💧 Water beats Gun!"

            else:

                detail = "🔫 Gun beats Snake!"

            self.user_score += 1

        # COMPUTER WINS

        else:

            result = "😢 YOU LOSE!"

            color = "#ff5f87"

            if computer == 1:

                detail = "🐍 Snake beats Water!"

            elif computer == -1:

                detail = "💧 Water beats Gun!"

            else:

                detail = "🔫 Gun beats Snake!"

            self.computer_score += 1

        # Result

        self.result_label.configure(
            text=result,
            fg=color
        )

        self.detail_label.configure(
            text=detail
        )

        # Score

        self.user_score_label.configure(
            text=f"YOU\n{self.user_score}"
        )

        self.computer_score_label.configure(
            text=f"COMPUTER\n{self.computer_score}"
        )

        round_number = (
            self.user_score
            + self.computer_score
            + 1
        )

        self.round_label.configure(
            text=f"ROUND {round_number}"
        )

        self.animate_result(color)

        self.round_active = False

    # ========================================================
    # RESULT ANIMATION
    # ========================================================

    def animate_result(self, color):

        self.result_frame.configure(
            highlightbackground=color
        )

        animation_id = self.root.after(
            180,
            lambda:
            self.result_frame.configure(
                highlightbackground="#8b5cf6"
            )
        )

        self.animation_ids.append(
            animation_id
        )

    # ========================================================
    # PLAY AGAIN
    # ========================================================

    def reset_round(self):

        self.clear_animation()

        self.round_active = False

        self.user_icon.configure(
            text="❔"
        )

        self.user_choice_label.configure(
            text="Choose your weapon"
        )

        self.computer_icon.configure(
            text="❔"
        )

        self.computer_choice_label.configure(
            text="Waiting..."
        )

        self.result_label.configure(
            text="Choose your weapon!",
            fg="#f5f7ff"
        )

        self.detail_label.configure(
            text=(
                "Snake beats Water  •  "
                "Water beats Gun  •  "
                "Gun beats Snake"
            )
        )

        self.vs_label.configure(
            text="VS"
        )

        round_number = (
            self.user_score
            + self.computer_score
            + 1
        )

        self.round_label.configure(
            text=f"ROUND {round_number}"
        )

        self.user_score_label.configure(
            text=f"YOU\n{self.user_score}"
        )

        self.computer_score_label.configure(
            text=f"COMPUTER\n{self.computer_score}"
        )

        # Reset button appearance

        for button in self.choice_buttons.values():

            button.configure(
                bg="#10243a"
            )

            button.icon_label.configure(
                bg="#10243a"
            )

            button.text_label.configure(
                bg="#10243a"
            )

    # ========================================================
    # CLEAR ANIMATIONS
    # ========================================================

    def clear_animation(self):

        for animation_id in self.animation_ids:

            try:
                self.root.after_cancel(
                    animation_id
                )

            except Exception:
                pass

        self.animation_ids.clear()


# ============================================================
# START GAME
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    game = SnakeWaterGun(root)

    root.mainloop()