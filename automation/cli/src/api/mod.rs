//! API client and data types

mod html;
mod tips;
mod waitlist;

pub use html::generate_newsletter_html;
pub use tips::{load_tips_from_files, Tip};
pub use waitlist::{Stats, WaitlistClient};
