import streamlit as st
import yaml
from datetime import date, timedelta
from fetch_gifts import fetch_gift_recommendations
from local_llm import generate_gift_suggestions

# Load options from YAML file
def load_yaml(filename="options.yml"):
    with open(filename, "r") as file:
        return yaml.safe_load(file)

options = load_yaml()

def dynamic_selection(label, key, options_list):
    """Handles selection with an 'Other' option that allows user input."""
    selection = st.selectbox(label, options_list + ["Other"], key=key)
    if selection == "Other":
        custom_value = st.text_input(f"Enter custom {label.lower()}", key=f"custom_{key}")
        if custom_value:
            return custom_value
    return selection

def dynamic_multiselect(label, key, options_list):
    """Handles multi-selection with an 'Other' option that allows user input."""
    selected = st.multiselect(label, options_list + ["Other"], key=key)
    if "Other" in selected:
        custom_value = st.text_input(f"Enter custom {label.lower()}", key=f"custom_{key}")
        if custom_value:
            selected.remove("Other")
            selected.append(custom_value)
    return selected

# Page Title
st.title("🎁 Thoughtful Gift Selector")
st.write("Find the perfect gift based on personality, interests, and more!")

# Occasion & Delivery Date
st.header("📅 Occasion & Delivery Details")
occasion = dynamic_selection("Select Occasion:", "occasion", options["occasions"])
delivery_date = st.date_input("Select Approximate Delivery Date:", min_value=date.today(), max_value=date.today() + timedelta(days=60))
formatted_date = delivery_date.strftime("%Y-%m-%d")

# Recipient
st.header("🎭 Recipient")
recipient = dynamic_selection("Who is the gift for?", "recipient", options["recipients"])

# Personal Interests & Hobbies
st.header("🎨 Personal Interests & Hobbies")
interests = dynamic_multiselect("What are their interests?", "interests", options["interests"])

# Lifestyle
st.header("🌿 Lifestyle")
lifestyle = dynamic_selection("How would you describe their lifestyle?", "lifestyle", options["lifestyles"])

# Needs or Wishlist
st.header("🛍 Needs & Wishlist")
needs = st.text_area("Have they mentioned anything they need or want?")

# Personality & Values
st.header("💖 Personality & Values")
values = dynamic_multiselect("What defines their personality?", "values", options["values"])

# Favorite Things
st.header("🌈 Favorite Things")
color = st.color_picker("Favorite Color:")
fav_things = st.text_input("Any favorite brands, books, movies, or foods?")

# Personality in Gifts
st.header("🎁 Gift Type Preferences")
gift_type = dynamic_selection("What type of gift would they appreciate most?", "gift_type", options["gift_types"])

# Budget
st.header("💰 Budget Consideration")
budget = st.slider("Select your budget range:", 10, 1000, (50, 200))

# Gift Presentation
st.header("🎀 Gift Presentation")
gift_wrap = dynamic_selection("Gift Wrap Options", "gift_wrap", options["gift_wraps"])
label = st.text_input("Custom Label or Message:")

# Gift Selection Method
st.header("🚀 Choose Your Gift-Finding Method")
method = st.radio(
    "Select how you'd like to find gifts:",
    [
        "🔍 Web Scraping + Sentiment Analysis (Automated)",
        "📢 Reddit/Twitter Trends + Local Stores (Unique)",
        "🤖 Local AI Model (Llama 2, GPT-J, GPT4All)"
    ]
)

# If "Local AI Model" is selected, show the model dropdown
if "Local AI Model" in method:
    model_type = st.selectbox("Select AI Model:", options["models"], key="model_type")

if st.button("🎉 Find Gift Suggestions"):
    st.success(f"Finding a perfect gift for {recipient} for {occasion}! Delivery by {delivery_date}.")
    
    # Generate search query based on user input
    prompt = f"What are the trending {gift_type} gift categories for {recipient}?"
    ecommerce_sites = options.get("ecommerce_sites", [])
    query = (
        f"Find **direct product links** to buy {gift_type} gift for {recipient}, "
        f"perfect for {lifestyle} lifestyle, "
        f"great for someone who loves {', '.join(interests) if interests else 'various interests'}, "
        f"aligned with {', '.join(values) if values else 'diverse'} values, "
        f"favorite color {color}. "
        f"Looking for {fav_things if fav_things else 'top-rated brands'}. "
        f"Budget: ${budget[0]} - ${budget[1]}. "
        f"Fast shipping available. "
        f"Direct purchase links only (no descriptions). "
        f"Only from these e-commerce sites: site:{' OR site:'.join(ecommerce_sites)}. "
        f"🔹 Return only clickable product links with a brief title (e.g., 'Black Personalized Necklace – [URL]'). "
        f"🔹 No summaries or reviews—only direct links."
    )

    print(query)

    st.session_state["query"] = query  # Store query for AI use
    
    if "Web Scraping" in method:
        st.write("### 🔍 Searching for best gifts...")
        gift_links = fetch_gift_recommendations(query)
        
        st.write("### 🎯 Recommended Gifts:")
        for i, link in enumerate(gift_links):
            st.markdown(f"[{i+1}. View Gift]({link})", unsafe_allow_html=True)

    elif "Reddit/Twitter" in method:
        st.write("🔎 **Check trending gift ideas on Reddit & Twitter!**")
        st.markdown("[🔗 Search Reddit for Gift Ideas](https://www.reddit.com/search/?q=unique+gift+ideas)", unsafe_allow_html=True)
        st.markdown("[🔗 Search Twitter Trends](https://twitter.com/search?q=gift+ideas&src=typed_query)", unsafe_allow_html=True)
        st.markdown("[🛒 Explore Local Stores](https://www.google.com/maps/search/gift+shops/)", unsafe_allow_html=True)

    elif "Local AI Model" in method:
        st.write(f"🤖 **Generating AI-powered gift recommendations using {model_type}...**")
        with st.spinner("Thinking... 🤔"):
            ai_suggestions = generate_gift_suggestions(query, model_type)
            st.success("🎁 AI Gift Suggestions:")
            st.write(ai_suggestions)

    st.balloons()