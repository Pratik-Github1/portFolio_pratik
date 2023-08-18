const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);
let activeCell;

const updateFollower = (cell, follower, left, top) => {
    const cellRect = cell.getBoundingClientRect();
    const [cellLeft, cellTop] = [cellRect.left, cellRect.top];
    const [cellWidth, cellHeight] = [cellRect.width, cellRect.height];

    follower.style.left = `${Math.round(((left - cellLeft) / cellWidth) * 100)}%`;
    follower.style.top = `${Math.round(((top - cellTop) / cellHeight) * 100)}%`;
};

const createFollower = (cell, x, y) => {
    const f = document.createElement("aside");
    f.classList.add("follower");
    updateFollower(cell, f, x, y);
    cell.appendChild(f);
};

const handleFollower = (e, cell) => {
    const [initx, inity] = [e.clientX, e.clientY];
    activeCell = cell;
    createFollower(cell, initx, inity);
    const follower = $(".follower");

    const handleMouseMove = (e) => {
        updateFollower(cell, follower, e.clientX, e.clientY);

        if (cell !== activeCell || !follower) {
            if (follower) {
                follower.remove();
            }
            activeCell = null;
            document.removeEventListener("mousemove", handleMouseMove);
            return;
        }
    };
    document.addEventListener("mousemove", handleMouseMove);
};

const handleMouseover = (e) => {
    const c = e.target.closest(".cell");
    handleFollower(e, c);
};

const handleMouseout = (e) => {
    const followers = $$(".follower");
    if (followers) {
        followers.forEach((follower) => follower.remove());
    }
};

$$(".cell").forEach((cell) => {
    cell.onmouseover = handleMouseover;
    cell.onmouseout = handleMouseout;
});