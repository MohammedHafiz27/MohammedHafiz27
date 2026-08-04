import os

os.environ.setdefault("GIFOS_GENERAL_COLOR_SCHEME", "catppuccin-mocha")
os.environ.setdefault("GIFOS_GENERAL_USER_NAME", "mohammedhafiz27")

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import gifos

FONT_FILE_BITMAP = os.path.join(os.path.dirname(gifos.__file__), "fonts", "gohufont-uni-14.pil")
FONT_FILE_LOGO = "./fonts/LogoFont-Bold.ttf"
CAT_IMAGE = "./cat.png"

GITHUB_USERNAME = "MohammedHafiz27"
IGNORE_REPOS = []


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_fps(13)  # set as int in code — env var GIFOS_GENERAL_FPS loads as a string and breaks math internally

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(timezone.utc).strftime("%Y")
    t.gen_text("GIF_OS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mHafiz Softwares Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Flutter(tm) GIFCPU - 250Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):
        t.delete_row(7)
        if i < 30000:
            t.gen_text(f"Memory Test: {i}", 7, count=2, contin=True)
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    # --- Boot splash with scramble logo effect ---
    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)
    t.set_font(FONT_FILE_LOGO, 66)
    logo_text = "HAFIZ"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(logo_text, 3, include_special=False)
    for line in effect_lines:
        t.delete_row(mid_row + 1)
        t.gen_text(line, mid_row + 1, mid_col + 1)

    # --- Login simulation ---
    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mHafiz OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("mohammedhafiz", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Africa/Cairo")).strftime("%a %b %d %I:%M:%S %p %Z %Y")
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    git_user_details = gifos.utils.fetch_github_stats(GITHUB_USERNAME, IGNORE_REPOS)
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    user_details_lines = f"""
    \x1b[30;101mMohammedHafiz27@GitHub\x1b[0m
    --------------
    \x1b[96mOS:      \x1b[93mWindows 11, macOS\x1b[0m
    \x1b[96mStack:   \x1b[93mFlutter, Dart, Go, Python\x1b[0m
    \x1b[96mEditor:  \x1b[93mVS Code + Antigravity\x1b[0m
    \x1b[96mArch:    \x1b[93mClean Architecture, BLoC/Cubit\x1b[0m

    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mEmail:      \x1b[93mmohammed.hafiz.2710@gmail.com\x1b[0m
    \x1b[96mLinkedIn:   \x1b[93mmohammedhafiz27\x1b[0m
    \x1b[96mPortfolio:  \x1b[93mmohammed-hafiz.vercel.app\x1b[0m

    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits ({int(year_now) - 1}): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs: \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %: \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[:5])}\x1b[0m
    """
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(f" -u {GITHUB_USERNAME}", 1, contin=True)

    t.toggle_show_cursor(False)
    # --- Paste the pixel-art cat ---
    t.paste_image(CAT_IMAGE, 3, 3, size_multiplier=0.55)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.toggle_show_cursor(True)
    t.gen_typing_text(
        "\x1b[92m# Have a nice day kind stranger :D Thanks for stopping by!",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=120, contin=True)

    t.gen_gif()
    print("INFO: output.gif generated")

    readme_file_content = rf"""<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./output.gif">
    <source media="(prefers-color-scheme: light)" srcset="./output.gif">
    <img alt="Terminal" src="output.gif">
</picture>

<sub><i>Generated automatically on {time_now}</i></sub>
</div>"""
    with open("README.md", "w") as f:
        f.write(readme_file_content)
        print("INFO: README.md file generated")


if __name__ == "__main__":
    main()
