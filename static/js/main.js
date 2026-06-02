document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------
    // 1. Dark/Light Theme Switcher
    // ----------------------------------------------------
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const currentTheme = localStorage.getItem('theme');

    // Function to set theme
    const setTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        
        // Update toggle button icon
        if (theme === 'dark') {
            if (themeIcon) themeIcon.className = 'bi bi-sun-fill';
        } else {
            if (themeIcon) themeIcon.className = 'bi bi-moon-stars-fill';
        }
    };

    // Initialize theme
    if (currentTheme) {
        setTheme(currentTheme);
    } else {
        // Fallback to system preference
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        setTheme(prefersDark ? 'dark' : 'light');
    }

    // Toggle listener
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const activeTheme = document.documentElement.getAttribute('data-theme');
            setTheme(activeTheme === 'dark' ? 'light' : 'dark');
        });
    }

    // ----------------------------------------------------
    // 2. Client-Side Project Filtering
    // ----------------------------------------------------
    const filterPills = document.querySelectorAll('.filter-pill');
    const projectCards = document.querySelectorAll('.project-card-col');

    if (filterPills.length > 0 && projectCards.length > 0) {
        // Add transitions styles for smooth filtering
        projectCards.forEach(card => {
            card.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
        });

        filterPills.forEach(pill => {
            pill.addEventListener('click', () => {
                // Remove active class from all pills and add to clicked one
                filterPills.forEach(p => p.classList.remove('active'));
                pill.classList.add('active');

                const filterValue = pill.getAttribute('data-filter');

                // Loop through projects and toggle visibility
                projectCards.forEach(card => {
                    const cardCategory = card.getAttribute('data-category');
                    
                    if (filterValue === 'all' || cardCategory === filterValue) {
                        card.style.display = 'block';
                        // Force reflow for transitions to trigger
                        void card.offsetWidth; 
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95)';
                        // Wait for transition to complete before setting display: none
                        const onTransitionEnd = (e) => {
                            if (e.propertyName === 'opacity' && card.style.opacity === '0') {
                                card.style.display = 'none';
                                card.removeEventListener('transitionend', onTransitionEnd);
                            }
                        };
                        card.addEventListener('transitionend', onTransitionEnd);
                    }
                });
            });
        });
    }

    // ----------------------------------------------------
    // 3. Client-Side Contact Form Validation
    // ----------------------------------------------------
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (event) => {
            let isValid = true;

            const nameInput = document.getElementById('contact-name');
            const emailInput = document.getElementById('contact-email');
            const messageInput = document.getElementById('contact-message');

            const nameError = document.getElementById('name-error');
            const emailError = document.getElementById('email-error');
            const messageError = document.getElementById('message-error');

            // Regex for email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            // Reset error messages and styles
            [nameError, emailError, messageError].forEach(err => {
                if (err) err.style.display = 'none';
            });
            [nameInput, emailInput, messageInput].forEach(inp => {
                if (inp) inp.classList.remove('is-invalid');
            });

            // Validate Name
            if (!nameInput || !nameInput.value.trim()) {
                if (nameInput) nameInput.classList.add('is-invalid');
                if (nameError) {
                    nameError.textContent = 'Please enter your name.';
                    nameError.style.display = 'block';
                }
                isValid = false;
            } else if (nameInput.value.trim().length < 2) {
                nameInput.classList.add('is-invalid');
                if (nameError) {
                    nameError.textContent = 'Name must be at least 2 characters long.';
                    nameError.style.display = 'block';
                }
                isValid = false;
            }

            // Validate Email
            if (!emailInput || !emailInput.value.trim()) {
                if (emailInput) emailInput.classList.add('is-invalid');
                if (emailError) {
                    emailError.textContent = 'Please enter your email address.';
                    emailError.style.display = 'block';
                }
                isValid = false;
            } else if (!emailRegex.test(emailInput.value.trim())) {
                emailInput.classList.add('is-invalid');
                if (emailError) {
                    emailError.textContent = 'Please enter a valid email address.';
                    emailError.style.display = 'block';
                }
                isValid = false;
            }

            // Validate Message
            if (!messageInput || !messageInput.value.trim()) {
                if (messageInput) messageInput.classList.add('is-invalid');
                if (messageError) {
                    messageError.textContent = 'Please enter a message.';
                    messageError.style.display = 'block';
                }
                isValid = false;
            } else if (messageInput.value.trim().length < 10) {
                messageInput.classList.add('is-invalid');
                if (messageError) {
                    messageError.textContent = 'Message must be at least 10 characters long.';
                    messageError.style.display = 'block';
                }
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault(); // Stop form submission
            }
        });
    }
});
