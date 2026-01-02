//! API client and data types

mod tips;
mod waitlist;

pub use tips::{load_tips_from_files, Tip};
pub use waitlist::{Stats, WaitlistClient};
