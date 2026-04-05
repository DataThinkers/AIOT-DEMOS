import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("🎯 Select Demo")

demo = st.sidebar.radio(
    "Choose Application",
    [
        "⚙️ Machine Monitoring",
        "🏠 Smart Home (Alexa)",
        "🪖 Military Surveillance",
        "🔄 IoT vs AIoT Comparison",
        "📡 IoT Architecture",
        "🚀 Kafka + Spark Pipeline",
        "⚡ Edge vs Cloud Decision"
    ]
)

# =========================================================
# DEMO 1: MACHINE MONITORING (NO ML LIB)
# =========================================================
if demo == "⚙️ Machine Monitoring":

    st.markdown("""
    <div style="background: linear-gradient(90deg, #00c6ff, #0072ff);
    padding:20px;border-radius:15px;color:white;text-align:center;
    font-size:22px;font-weight:bold;">
    ⚙️ Machine Monitoring (Pattern-Based Detection)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Simulate normal data
    np.random.seed(42)
    vibration = np.random.normal(5, 1, 100)
    temperature = np.random.normal(50, 5, 100)

    data = pd.DataFrame({
        "Vibration": vibration,
        "Temperature": temperature
    })

    # Learn normal range (mean + std)
    vib_mean = data["Vibration"].mean()
    vib_std = data["Vibration"].std()

    temp_mean = data["Temperature"].mean()
    temp_std = data["Temperature"].std()

    col1, col2 = st.columns(2)

    # LEFT → NORMAL DATA
    with col1:
        st.subheader("📊 Learned Normal Behaviour")

        st.dataframe(data.style.background_gradient(cmap="Blues"))

        st.write("📌 Normal Range:")
        st.write(f"Vibration: {vib_mean:.2f} ± {vib_std:.2f}")
        st.write(f"Temperature: {temp_mean:.2f} ± {temp_std:.2f}")

    # RIGHT → LIVE INPUT
    with col2:
        st.subheader("📡 Live Sensor Input")

        v = st.slider("Vibration", 0.0, 15.0, 5.0)
        t = st.slider("Temperature", 20.0, 100.0, 50.0)

        # Simple anomaly logic
        vib_anomaly = abs(v - vib_mean) > 2 * vib_std
        temp_anomaly = abs(t - temp_mean) > 2 * temp_std

        st.subheader("🧠 System Decision")

        if vib_anomaly or temp_anomaly:
            st.error("⚠️ Anomaly Detected (Out of Normal Range)")
        else:
            st.success("✅ Normal Operation")

# =========================================================
# DEMO 2: ALEXA
# =========================================================
elif demo == "🏠 Smart Home (Alexa)":

    st.markdown("""
    <div style="background: linear-gradient(90deg, #ff7e5f, #feb47b);
    padding:20px;border-radius:15px;color:white;text-align:center;
    font-size:22px;font-weight:bold;">
    🏠 Smart Home Assistant (Alexa Simulation)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if "light" not in st.session_state:
        st.session_state.light = False

    if "fan" not in st.session_state:
        st.session_state.fan = False

    cmd = st.text_input("🎤 Say: Turn on light / Turn off fan")

    if st.button("Execute"):
        c = cmd.lower()

        if "light" in c and "on" in c:
            st.session_state.light = True
            st.success("💡 Light ON")

        elif "light" in c and "off" in c:
            st.session_state.light = False
            st.warning("💡 Light OFF")

        elif "fan" in c and "on" in c:
            st.session_state.fan = True
            st.success("🌀 Fan ON")

        elif "fan" in c and "off" in c:
            st.session_state.fan = False
            st.warning("🌀 Fan OFF")

        else:
            st.error("Command not recognized")

    colA, colB = st.columns(2)
    colA.metric("💡 Light", "ON" if st.session_state.light else "OFF")
    colB.metric("🌀 Fan", "ON" if st.session_state.fan else "OFF")

# =========================================================
# DEMO 3: MILITARY
# =========================================================
elif demo == "🪖 Military Surveillance":

    from sklearn.ensemble import IsolationForest

    st.markdown("""
    <div style="background: linear-gradient(90deg, #1f3c88, #6a11cb);
    padding:20px;border-radius:15px;color:white;text-align:center;
    font-size:22px;font-weight:bold;">
    🪖 AI-Enabled Battlefield Surveillance (ML-Based)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # =========================================================
    # TRAIN NORMAL DATA
    # =========================================================
    import numpy as np
    import pandas as pd

    np.random.seed(42)

    normal_data = pd.DataFrame({
        "Distance": np.random.normal(12, 3, 100),
        "Speed": np.random.normal(60, 20, 100),
        "Heat": np.random.normal(40, 10, 100),
        "Motion": np.random.normal(30, 10, 100)
    })

    model = IsolationForest(contamination=0.1)
    model.fit(normal_data)

    # =========================================================
    # UI LAYOUT
    # =========================================================
    col1, col2 = st.columns(2)

    # LEFT SIDE → TRAINING
    with col1:
        st.subheader("📊 Learned Normal Battlefield Patterns")
        st.dataframe(normal_data.style.background_gradient(cmap="Purples"))

    # RIGHT SIDE → LIVE INPUT
    with col2:
        st.subheader("🎮 Live Surveillance Input")

        d = st.slider("🚁 Drone Distance (km)", 0.5, 20.0, 10.0)
        s = st.slider("⚡ Drone Speed (km/h)", 10, 300, 80)
        h = st.slider("🌡 Thermal Signature", 0, 100, 40)
        m = st.slider("🎯 Movement Level", 0, 100, 30)

        input_data = [[d, s, h, m]]

        pred = model.predict(input_data)

        st.subheader("🧠 AI Threat Analysis")

        if pred[0] == -1:
            st.markdown("""
            <div style="
                background:#ff4d4d;
                padding:25px;
                border-radius:15px;
                color:white;
                text-align:center;
                font-size:22px;
                font-weight:bold;">
                🚨 THREAT DETECTED<br>
                Abnormal Pattern Identified
            </div>
            """, unsafe_allow_html=True)

            st.warning("⚡ Action: Alert command center & activate defense")

        else:
            st.markdown("""
            <div style="
                background:#2ecc71;
                padding:25px;
                border-radius:15px;
                color:white;
                text-align:center;
                font-size:22px;
                font-weight:bold;">
                ✅ NORMAL ACTIVITY<br>
                Area Under Control
            </div>
            """, unsafe_allow_html=True)

    # =========================================================
    # FLOW
    # =========================================================
    st.markdown("---")
    st.write("🔄 Flow: Sensors → Data → ML Model → Threat Detection → Action")

elif demo == "🔄 IoT vs AIoT Comparison":

    from sklearn.ensemble import IsolationForest
    import numpy as np
    import pandas as pd

    st.markdown("""
    <div style="background: linear-gradient(90deg, #ff9966, #ff5e62);
    padding:20px;border-radius:15px;color:white;text-align:center;
    font-size:22px;font-weight:bold;">
    🔄 Traditional IoT vs AIoT
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # =========================================================
    # SENSOR INPUT
    # =========================================================
    st.subheader("📡 Sensor Input")

    colA, colB = st.columns(2)

    with colA:
        temp = st.slider("🌡 Temperature", 0, 100, 50)

    with colB:
        vibration = st.slider("⚙️ Vibration", 0, 20, 5)

    st.markdown("---")

    # =========================================================
    # TWO SYSTEMS
    # =========================================================
    col1, col2 = st.columns(2)

    # -----------------------------
    # TRADITIONAL IoT
    # -----------------------------
    with col1:
        st.markdown("### ❌ Traditional IoT")

        st.info("Monitoring Dashboard (Human Decision)")

        # Dashboard view
        st.metric("Temperature", temp)
        st.metric("Vibration", vibration)

        st.markdown("""
        <div style="
            background:#f4f4f4;
            padding:15px;
            border-radius:10px;
            text-align:center;">
            👨‍💻 Human observes data and decides action
        </div>
        """, unsafe_allow_html=True)

        st.warning("➡️ No automatic decision")

    # -----------------------------
    # AIoT SYSTEM
    # -----------------------------
    with col2:
        st.markdown("### ✅ AIoT System")

        st.info("AI-Based Automatic Decision")

        # Train model
        np.random.seed(42)
        data = pd.DataFrame({
            "Temp": np.random.normal(50, 10, 100),
            "Vibration": np.random.normal(5, 2, 100)
        })

        model = IsolationForest(contamination=0.1)
        model.fit(data)

        pred = model.predict([[temp, vibration]])

        if pred[0] == -1:
            st.markdown("""
            <div style="
                background:#ff4d4d;
                padding:20px;
                border-radius:12px;
                color:white;
                text-align:center;
                font-weight:bold;">
                ⚠️ ANOMALY DETECTED<br>
                🔧 Action: System triggers cooling
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="
                background:#2ecc71;
                padding:20px;
                border-radius:12px;
                color:white;
                text-align:center;
                font-weight:bold;">
                ✅ NORMAL<br>
                ⚙️ System continues operation
            </div>
            """, unsafe_allow_html=True)

    # =========================================================
    # FINAL MESSAGE
    # =========================================================
    st.markdown("---")

    st.markdown("""
    <div style="
        background:#e6f2ff;
        padding:20px;
        border-radius:12px;
        text-align:center;
        font-size:18px;
        font-weight:bold;">
        IoT → Monitoring (Human in Loop) 📊<br><br>
        AIoT → Intelligence + Automation 🧠⚙️
    </div>
    """, unsafe_allow_html=True)


elif demo == "📡 IoT Architecture":

    import random
    import streamlit as st

    st.set_page_config(layout="wide")

    # =========================================================
    # TITLE
    # =========================================================
    st.markdown("## 📡 IoT Architecture Simulation")

    st.markdown("---")

    # =========================================================
    # STEP 1: Sensors, Actuators & Devices
    # =========================================================
    st.subheader("1️⃣ Sensors, Actuators & Devices")

    temp = random.randint(20, 80)
    humidity = random.randint(30, 90)

    col1, col2 = st.columns(2)
    col1.metric("🌡 Temperature Sensor", temp)
    col2.metric("💧 Humidity Sensor", humidity)

    st.info("Devices collect real-world data")

    st.markdown("---")

    # =========================================================
    # STEP 2: Gateway
    # =========================================================
    st.subheader("2️⃣ Gateway")

    st.success("📡 Gateway aggregates and forwards data")

    st.markdown("---")

    # =========================================================
    # STEP 3: Wide Area Network
    # =========================================================
    st.subheader("3️⃣ Wide Area Network")

    st.warning("🌐 Data transmitted via Internet")

    st.markdown("---")

    # =========================================================
    # STEP 4: M2M Manager / Cloud Server (AI Layer)
    # =========================================================
    st.subheader("4️⃣ M2M Manager / Cloud Server (AI Intelligence Layer)")

    st.write("💾 Data Processing | 🌐 Web Server | 🧠 ML Model")

    if temp > 60:
        ai_status = "High Temperature Pattern"
        st.warning("🧠 AI Insight: High temperature detected")
    else:
        ai_status = "Normal Pattern"
        st.success("🧠 AI Insight: Normal condition")

    st.markdown("---")

    # =========================================================
    # STEP 5: MOBILE APP UI (CLEAN VERSION)
    # =========================================================
    st.subheader("5️⃣ User Interaction (Mobile App)")

    colA, colB, colC = st.columns([1, 2, 1])

    with colB:
        st.markdown("### 📱 Smart Home App")

        with st.container(border=True):

            st.metric("🌡 Temperature", f"{temp}°C")
            st.metric("💧 Humidity", f"{humidity}%")
            st.metric("🧠 AI Status", ai_status)

            device = st.toggle("⚙️ Device Control")

            if device:
                st.success("Device ON (User Controlled)")
            else:
                st.info("Device OFF")

    st.warning("👨‍💻 IoT: User monitors and controls system manually")

    st.markdown("---")

    # =========================================================
    # STEP 6: AIoT AUTOMATION
    # =========================================================
    st.subheader("⚙️ Automated Processes (AIoT)")

    if temp > 60:
        st.error("🔥 AIoT Action: Cooling Activated Automatically")
    else:
        st.success("✅ System Running Normally")

    st.markdown("---")

    # =========================================================
    # FLOW
    # =========================================================
    st.info("🔄 Flow: Sensors → Gateway → Network → Cloud (AI) → User → Automation")


elif demo == "🚀 Kafka + Spark Pipeline":

    import streamlit as st
    import random
    import time
    import pandas as pd

    st.markdown("## 🚀 Kafka + Spark (Real Streaming with Buffer)")

    st.write("Kafka buffers data between fast sensors and slower processing")

    st.markdown("---")

    # =========================
    # SESSION STATE
    # =========================
    if "kafka_queue" not in st.session_state:
        st.session_state.kafka_queue = []

    if "processed" not in st.session_state:
        st.session_state.processed = pd.DataFrame(
            columns=["Temperature", "Result"]
        )

    if "running" not in st.session_state:
        st.session_state.running = False

    # =========================
    # CONTROLS
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("▶ Start"):
        st.session_state.running = True

    if col2.button("⏹ Stop"):
        st.session_state.running = False

    # =========================
    # PLACEHOLDER UI
    # =========================
    placeholder = st.empty()

    # =========================
    # STREAM LOOP
    # =========================
    while st.session_state.running:

        # 🔥 FAST PRODUCER (Kafka input)
        for _ in range(2):  # add multiple messages
            temp = random.randint(20, 90)
            st.session_state.kafka_queue.append(temp)

        # 🧠 SLOW CONSUMER (Spark)
        if st.session_state.kafka_queue:
            data = st.session_state.kafka_queue.pop(0)

            if data > 60:
                result = "⚠️ Anomaly"
            else:
                result = "✅ Normal"

            new_row = pd.DataFrame({
                "Temperature": [data],
                "Result": [result]
            })

            st.session_state.processed = pd.concat(
                [st.session_state.processed, new_row],
                ignore_index=True
            )

        # =========================
        # UI UPDATE
        # =========================
        with placeholder.container():

            colA, colB = st.columns(2)

            with colA:
                st.subheader("📡 Sensor + Kafka")

                if st.session_state.kafka_queue:
                    st.metric("Latest Incoming", st.session_state.kafka_queue[-1])

                st.write("📦 Kafka Queue:")
                st.write(st.session_state.kafka_queue)

                st.write(f"📊 Queue Size: {len(st.session_state.kafka_queue)}")

            with colB:
                st.subheader("🧠 Spark Processing")

                st.dataframe(
                    st.session_state.processed.tail(5),
                    use_container_width=True
                )

            st.markdown("---")
            st.info("🔄 Flow: Sensor → Kafka (Buffer) → Spark")

        time.sleep(1)


elif demo == "⚡ Edge vs Cloud Decision":

    import streamlit as st
    import random
    import time
    import pandas as pd
    from datetime import datetime

    st.markdown("## ⚡ Edge vs Cloud + Contextualization (Smart Decision)")

    st.write("System decides based on urgency, not just raw values")

    st.markdown("---")

    # =========================
    # SESSION STATE
    # =========================
    if "logs" not in st.session_state:
        st.session_state.logs = pd.DataFrame(
            columns=["Time", "Device", "Location", "Temperature", "Urgency", "Decision", "Latency"]
        )

    if "running" not in st.session_state:
        st.session_state.running = False

    # =========================
    # CONTROLS
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("▶ Start"):
        st.session_state.running = True

    if col2.button("⏹ Stop"):
        st.session_state.running = False

    placeholder = st.empty()

    # =========================
    # STREAM LOOP
    # =========================
    while st.session_state.running:

        # RAW DATA
        temp = random.randint(20, 90)

        # =========================
        # CONTEXTUALIZATION
        # =========================
        timestamp = datetime.now().strftime("%H:%M:%S")
        device = "Sensor-A"
        location = "Factory Floor"

        # =========================
        # URGENCY LOGIC (NEW)
        # =========================
        if temp > 75:
            urgency = "High"
        elif temp > 55:
            urgency = "Medium"
        else:
            urgency = "Low"

        # =========================
        # DECISION BASED ON URGENCY
        # =========================
        if urgency == "High":
            decision = "⚡ Edge"
            latency = "1 ms"
            action = "🔥 Emergency Cooling Activated"
        else:
            decision = "☁️ Cloud"
            latency = "200 ms"
            action = "📊 Sent for Analytics"

        # =========================
        # STORE DATA
        # =========================
        new_row = pd.DataFrame({
            "Time": [timestamp],
            "Device": [device],
            "Location": [location],
            "Temperature": [temp],
            "Urgency": [urgency],
            "Decision": [decision],
            "Latency": [latency]
        })

        st.session_state.logs = pd.concat(
            [st.session_state.logs, new_row],
            ignore_index=True
        )

        # =========================
        # UI UPDATE
        # =========================
        with placeholder.container():

            colA, colB = st.columns(2)

            with colA:
                st.subheader("📡 Sensor Data")
                st.metric("Temperature", temp)

            with colB:
                st.subheader("🧠 Smart Decision")
                st.write(f"Urgency: {urgency}")
                st.write(f"Decision: {decision}")
                st.write(f"Latency: {latency}")

            st.markdown("---")

            # Show reason clearly
            st.info(f"📌 Reason: {urgency} urgency data → processed at {decision}")

            if urgency == "High":
                st.error(action)
            else:
                st.success(action)

            st.markdown("---")

            st.subheader("📊 Contextualized Data (AI-Ready)")
            st.dataframe(
                st.session_state.logs.tail(10),
                use_container_width=True
            )

            st.info("🔄 Flow: Sensor → Context → Decision → Edge/Cloud → Action")

        time.sleep(1)
