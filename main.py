#!/usr/bin/env python3
from safe32 import safe32_encode, safe32_decode
import struct
import argparse

def item_serializer(batch_size: int, batch_index: int, batch_id: int) -> bytes:
    """generate safe32 encoded serial number for item

    Args:
        batch_size (int): number items in batch
        batch_index (int): which item from batch
        batch_id (int): which batch (sequential)

    Raises:
        Exception: batch size too large
        Exception: batch id too large
        Exception: batch index larger than batch size

    Returns:
        bytes: serial as bytes
    """
    if batch_size > 255:
        raise Exception("batch size too large, must be less than or equal 255")
    elif batch_id > 255:
        raise Exception("batch id too large, must be less than or equal 255")
    elif batch_index > batch_size:
        raise Exception("batch index larger than batch index")
    
    raw_info = struct.pack("BBB", batch_size, batch_index, batch_id)

    return safe32_encode(raw_info)

def item_deserializer(serial: bytes | str) -> tuple[int, int, int]:
    """get information for item from serial

    Args:
        serial (bytes | str): item serial string

    Raises:
        Exception: unable to decode serial

    Returns:
        tuple[int, int, int]: tuple of (batch_size, batch_index, batch_id)
    """
    
    raw_info = safe32_decode(serial)
    batch_size, batch_index, batch_id = struct.unpack("BBB", raw_info)

    return (batch_size, batch_index, batch_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serial", "-s", type=str, help="serial string to decode")

    parser.add_argument("--batch-size", "-z", type=int, help="batch size to encode")
    parser.add_argument("--batch-index", "-n", type=int, help="batch index to encode")
    parser.add_argument("--batch-id", "-i", type=int, help="batch id to encode")

    args = parser.parse_args()

    serial: str | None = args.serial

    batch_size: int | None = args.batch_size
    batch_index: int | None = args.batch_index
    batch_id: int | None = args.batch_id

    if serial is not None:
            batch_size, batch_index, batch_id = item_deserializer(serial)
            print("item info:")
            print(f"  {'batch size:':<15}{batch_size:>4}")
            print(f"  {'batch index:':<15}{batch_index:>4}")
            print(f"  {'batch id:':<15}{batch_id:>4}")
    elif batch_id is not None and batch_index is not None and batch_id is not None:
            print(f"item serial:  {item_serializer(batch_size, batch_index, batch_id).decode()}")