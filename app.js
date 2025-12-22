// Import Firebase SDK (CDN)
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getDatabase, ref, onValue, runTransaction, set } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";

// ... (existing config matches) ...

// ... (rest of code) ...

// ==========================================
// 🔥 FIREBASE 설정 (선생님께서 여기에 키를 넣어주세요!)
// ==========================================
const firebaseConfig = {
    // 여기에 복사한 내용을 붙여넣으세요! (apiKey, authDomain 등)
    // 예: apiKey: "AIzaSyD...",
    apiKey: "AIzaSyDYgasf-YgTB_xr99J2iDgb4PP8KsaIwxc",
    authDomain: "app-test-7b6c7.firebaseapp.com",
    databaseURL: "https://app-test-7b6c7-default-rtdb.firebaseio.com",
    projectId: "app-test-7b6c7",
    storageBucket: "app-test-7b6c7.firebasestorage.app",
    messagingSenderId: "1014651386395",
    appId: "1:1014651386395:web:0b78856d0e8f67acc0d6be",
    measurementId: "G-M0JRC64R44"
};

// Initialize Firebase
let db = null;
try {
    // Basic check to see if user updated config
    if (firebaseConfig.apiKey !== "YOUR_API_KEY") {
        const app = initializeApp(firebaseConfig);
        db = getDatabase(app);
        console.log("Firebase Connected!");
    } else {
        console.warn("Firebase Config not set.");
    }
} catch (e) {
    console.error("Firebase Init Error:", e);
}


document.addEventListener('DOMContentLoaded', async () => {
    // Snow Effect Logic
    function createSnow() {
        const container = document.createElement('div');
        container.className = 'snow-container';
        document.body.appendChild(container);

        setInterval(() => {
            const snowflake = document.createElement('div');
            snowflake.className = 'snowflake';

            // Random size 2px - 5px
            const size = Math.random() * 3 + 2;
            snowflake.style.width = `${size}px`;
            snowflake.style.height = `${size}px`;

            // Random position
            snowflake.style.left = `${Math.random() * 100}vw`;

            // Random opacity
            snowflake.style.opacity = Math.random() * 0.5 + 0.3;

            // Random speed 3s - 8s
            const duration = Math.random() * 1 + 8;
            snowflake.style.animationDuration = `${duration}s`;

            container.appendChild(snowflake);

            // Remove after animation
            setTimeout(() => {
                snowflake.remove();
            }, duration * 1000);
        }, 100); // Create snowflake every 100ms
    }
    createSnow();

    const galleryContainer = document.querySelector('.bento-container');
    const modal = document.getElementById('code-modal');
    const closeModal = document.getElementById('close-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalTag = document.getElementById('modal-tag');
    const codeBlock = document.getElementById('code-block');
    const downloadBtn = document.getElementById('download-btn');

    // Create new elements for Modal Footer (Like Button)
    const modalFooter = document.querySelector('.modal-footer');
    // Clear existing to rebuild correctly with like button
    // But we want to keep download button logic.
    // Let's modify the HTML structure dynamically or just inject.
    // Structure: [Like Button] [File Info] [Download]
    // Current Modal Footer HTML: 
    // <div class="file-info">...</div> <a id="download-btn">...</a>

    // Let's adjust modalFooter in JS to add the big like button
    const likeWrapper = document.createElement('div');
    likeWrapper.className = 'modal-like-wrapper';

    const bigLikeBtn = document.createElement('button');
    bigLikeBtn.className = 'big-like-btn';
    bigLikeBtn.innerHTML = `
        <svg class="like-icon" viewBox="0 0 24 24">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
        <span id="modal-like-count">0</span> LIKES
    `;
    likeWrapper.appendChild(bigLikeBtn);

    // Insert before the download button
    modalFooter.insertBefore(likeWrapper, downloadBtn);


    // Fetch manifest
    let projects = [];
    try {
        const response = await fetch('manifest.json');
        projects = await response.json();
    } catch (error) {
        galleryContainer.innerHTML = '<p style="text-align:center; color:red;">프로젝트 목록 로딩 실패 (manifest.json)</p>';
        return;
    }

    // Prepare Data Structure
    const projectData = projects.map(filename => {
        let displayName = filename.replace('.py', '').replace('.PY', '');

        // Hash for deterministic properties
        let hash = 0;
        for (let i = 0; i < filename.length; i++) {
            hash = filename.charCodeAt(i) + ((hash << 5) - hash);
        }

        const icons = [
            '🛸', '🚀', '⭐', '🪐', '🌌', '🎨', '🎮', '🕹️', '🎲', '🧩',
            '🤖', '👾', '👻', '🐲', '🦄', '🦁', '🦊', '🐨', '🐼', '🐯',
            '🌵', '🍀', '🍄', '🌸', '🌹', '🌺', '🌻', '🏔️', '🌋', '🏝️',
            '🏰', '🗽', '🎡', '🎢', '🎪', '🎭', '🧶', '🧵', '🎼', '🎹',
            '🥁', '🎷', '🎸', '🎺', '🎻', '💾', '💿', '📀', '💎', '🔮',
            '🧬', '🔬', '🔭', '🧪', '🩸', '💊', '🩹', '🧱', '🧲', '🧨'
        ];

        const genres = ['RPG', 'Action', 'Puzzle', 'Simulation', 'Arcade', 'Adventure', 'Strategy', 'Shooter'];

        return {
            filename,
            title: displayName,
            icon: icons[Math.abs(hash) % icons.length],
            colorStart: Math.abs(hash) % 360,
            genre: genres[Math.abs(hash) % genres.length],
            // Base rating 4.2, will update with likes
            rating: 4.2,
            baseHash: hash,
            likes: 0 // Will fetch from DB
        };
    });

    // Validates rating max 5.0
    function calculateRating(likes) {
        // Base 4.2 + 0.1 per like. Max 5.0
        const r = 4.2 + (likes * 0.1);
        return Math.min(5.0, r).toFixed(1);
    }

    // Render Function
    function renderGallery() {
        galleryContainer.innerHTML = '';

        // Sort by Likes to determine size?
        // User asked: "Order by likes count, and size changes"
        // Let's sort copy of array to find top 3
        const sorted = [...projectData].sort((a, b) => b.likes - a.likes);
        const top3 = sorted.slice(0, 3).map(p => p.filename);

        projectData.forEach(p => {
            // Update rating based on current likes
            p.rating = calculateRating(p.likes);

            const isTop = top3.includes(p.filename) && p.likes > 0; // Only resize if actually liked

            // Checks if CURRENT user liked this
            const isLiked = localStorage.getItem(`liked_${p.filename}`) === 'true';

            // Grid Size Logic
            // If Top 3 and has likes -> Large or Wide
            // Else -> Random small/wide based on hash mechanism

            let spanClass = '';
            if (isTop) {
                if (p.filename === top3[0]) spanClass = 'span-large'; // #1
                else spanClass = 'span-wide'; // #2, #3
            } else {
                // Original deterministic sizing
                const sizeRoll = Math.abs(p.baseHash * 7) % 100;
                if (sizeRoll < 15) spanClass = 'span-wide';
                else spanClass = '';
            }

            const gradient = `linear-gradient(135deg, hsl(${p.colorStart}, 70%, 60%), hsl(${(p.colorStart + 40) % 360}, 70%, 60%))`;
            const likeBtnClass = isLiked ? 'like-btn liked' : 'like-btn';

            const card = document.createElement('div');
            card.className = `gallery-item ${spanClass}`;
            card.innerHTML = `
                <div class="like-container">
                    <button class="${likeBtnClass}" onclick="event.stopPropagation(); toggleLike('${p.filename}')">
                        <svg class="like-icon" viewBox="0 0 24 24">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                        </svg>
                    </button>
                    <span class="like-count">${p.likes}</span>
                </div>
                <div class="item-visual">
                    <div class="item-icon-wrapper" style="background: ${gradient}">
                        <div class="item-icon">${p.icon}</div>
                    </div>
                </div>
                <div class="item-info">
                    <div class="item-tags">
                        <span class="tag">${p.genre}</span>
                        <span class="tag">Python</span>
                    </div>
                    <div class="item-title">${p.title}</div>
                    <div class="item-rating">⭐ ${p.rating}</div>
                </div>
            `;

            card.addEventListener('click', () => openProject(p));
            galleryContainer.appendChild(card);
        });
    }

    // Initial Render
    renderGallery();

    // Listen to Firebase Realtime Database
    if (db) {
        const likesRef = ref(db, 'likes');
        onValue(likesRef, (snapshot) => {
            const data = snapshot.val() || {};
            let changed = false;
            projectData.forEach(p => {
                // sanitize filename for DB key (remove . etc) or just use as is if supported?
                // Firebase keys cannot contain . # $ [ ]
                // So we format key: replace . with _
                const key = p.filename.replace(/\./g, '_');
                const newLike = data[key] || 0;
                if (p.likes !== newLike) {
                    p.likes = newLike;
                    changed = true;
                }
            });

            if (changed) {
                renderGallery();
                // If modal is open, update its like count too
                if (currentProject) {
                    const key = currentProject.filename.replace(/\./g, '_');
                    document.getElementById('modal-like-count').textContent = data[key] || 0;
                    // Also update modal button state just in case
                    const isLiked = localStorage.getItem(`liked_${currentProject.filename}`) === 'true';
                    if (isLiked) bigLikeBtn.classList.add('liked');
                    else bigLikeBtn.classList.remove('liked');
                }
            }
        });
    }

    // Like Action
    window.toggleLike = function (filename) {
        const localLikeKey = `liked_${filename}`;
        const isLiked = localStorage.getItem(localLikeKey) === 'true';
        console.log(`Toggling like for ${filename}. Currently liked? ${isLiked}`);

        if (!db) {
            // Demo Mode
            const p = projectData.find(x => x.filename === filename);
            if (p) {
                if (isLiked) {
                    p.likes = Math.max(0, p.likes - 1);
                    localStorage.removeItem(localLikeKey);
                } else {
                    p.likes++;
                    localStorage.setItem(localLikeKey, 'true');
                }
                renderGallery();
                if (currentProject && currentProject.filename === filename) {
                    const btn = document.querySelector('.big-like-btn');
                    if (localStorage.getItem(localLikeKey) === 'true') btn.classList.add('liked');
                    else btn.classList.remove('liked');
                    document.getElementById('modal-like-count').textContent = p.likes;
                }
            }
            return;
        }

        const key = filename.replace(/\./g, '_');
        const likeRef = ref(db, 'likes/' + key);

        if (isLiked) {
            localStorage.removeItem(localLikeKey);
        } else {
            localStorage.setItem(localLikeKey, 'true');
        }

        // Transaction
        runTransaction(likeRef, (currentLikes) => {
            if (isLiked) {
                // Was liked, so remove like
                return Math.max(0, (currentLikes || 0) - 1);
            } else {
                // Was not liked, so add like
                return (currentLikes || 0) + 1;
            }
        }).catch(err => {
            console.error("Like failed", err);
            // Revert local state if fail
            if (isLiked) localStorage.setItem(localLikeKey, 'true');
            else localStorage.removeItem(localLikeKey);
            renderGallery();
        });
    };

    // Global variable to track modal state
    let currentProject = null;

    async function openProject(p) {
        currentProject = p;
        modalTitle.textContent = p.title;
        modalTag.textContent = p.genre;
        codeBlock.textContent = '로딩 중...';
        codeBlock.className = 'language-python';

        // Update Modal Like Button state
        const modalLikeCount = document.getElementById('modal-like-count');
        modalLikeCount.textContent = p.likes;

        const isLiked = localStorage.getItem(`liked_${p.filename}`) === 'true';
        if (isLiked) bigLikeBtn.classList.add('liked');
        else bigLikeBtn.classList.remove('liked');

        // Update Download Link
        const filePath = `python%20folder/${encodeURIComponent(p.filename)}`;
        downloadBtn.href = `python%20folder/${p.filename}`;

        // Bind click to the big like button
        bigLikeBtn.onclick = () => window.toggleLike(p.filename);

        modal.classList.remove('hidden');
        requestAnimationFrame(() => {
            modal.classList.add('active');
        });

        try {
            const res = await fetch(`${filePath}?t=${new Date().getTime()}`);
            if (!res.ok) throw new Error('파일을 찾을 수 없습니다');
            const text = await res.text();
            codeBlock.textContent = text;
            Prism.highlightElement(codeBlock);
        } catch (err) {
            codeBlock.textContent = `코드 로딩 오류: ${err.message}`;
        }
    }

    function hideModal() {
        modal.classList.remove('active');
        setTimeout(() => {
            modal.classList.add('hidden');
            currentProject = null;
        }, 300);
    }

    closeModal.addEventListener('click', hideModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) hideModal();
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            hideModal();
        }
    });

    // ==========================================
    // 🛠️ 관리자 도구 (콘솔에서 사용)
    // F12 누르고 resetAllLikes() 치면 초기화
    // ==========================================
    window.resetAllLikes = function () {
        if (!confirm("정말 모든 좋아요를 0으로 초기화하시겠습니까?")) return;

        if (!db) {
            console.log("데모 모드: 로컬 스토리지 초기화");
            projectData.forEach(p => {
                p.likes = 0;
                localStorage.removeItem(`liked_${p.filename}`);
            });
            renderGallery();
            return;
        }

        projectData.forEach(p => {
            const key = p.filename.replace(/\./g, '_');
            set(ref(db, 'likes/' + key), 0);
        });
        console.log("모든 좋아요가 초기화되었습니다.");
    };
});
