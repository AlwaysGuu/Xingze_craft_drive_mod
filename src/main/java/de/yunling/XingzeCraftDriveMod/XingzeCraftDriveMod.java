package de.yunling.XingzeCraftDriveMod;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import de.yunling.XingzeCraftDriveMod.block.RailwaySignStop;
import de.yunling.XingzeCraftDriveMod.block.StationSignMc01;
import de.yunling.XingzeCraftDriveMod.block.StationSignMc02;
import de.yunling.XingzeCraftDriveMod.block.StationSignMc03;
import de.yunling.XingzeCraftDriveMod.block.StationSignMc04;
import de.yunling.XingzeCraftDriveMod.block.StationSignMc05;
import de.yunling.XingzeCraftDriveMod.block.StationSignMc06;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.client.itemgroup.FabricItemGroupBuilder;
import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.block.Material;

import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Identifier;

import net.minecraft.util.registry.Registry;

public class XingzeCraftDriveMod implements ModInitializer {
	// This logger is used to write text to the console and the log file.
	// It is considered best practice to use your mod id as the logger's name.
	// That way, it's clear which mod wrote info, warnings, and errors.
	public static final Logger LOGGER = LogManager.getLogger("modid");
	public static final Block Station_Sign_MC01 = new StationSignMc01(Block.Settings.of(Material.METAL).hardness(4.0F));
	public static final Block Station_Sign_MC02 = new StationSignMc02(Block.Settings.of(Material.METAL).hardness(4.0F));
	public static final Block Station_Sign_MC03 = new StationSignMc03(Block.Settings.of(Material.METAL).hardness(4.0F));
	public static final Block Station_Sign_MC04 = new StationSignMc04(Block.Settings.of(Material.METAL).hardness(4.0F));
	public static final Block Station_Sign_MC05 = new StationSignMc05(Block.Settings.of(Material.METAL).hardness(4.0F));
	public static final Block Station_Sign_MC06 = new StationSignMc06(Block.Settings.of(Material.METAL).hardness(4.0F));
	public static final Block railway_sign_stop = new RailwaySignStop(Block.Settings.of(Material.METAL).hardness(4.0F));

	@Override

	public void onInitialize() {
		// This code runs as soon as Minecraft is in a mod-load-ready state.
		// However, some things (like resources) may still be uninitialized.
		// Proceed with mild caution.
		Registry.register(Registry.BLOCK, new Identifier("xcdm", "station_sign_mc01"), Station_Sign_MC01);
		Registry.register(Registry.ITEM, new Identifier("xcdm", "station_sign_mc01"),
				new BlockItem(Station_Sign_MC01, new Item.Settings().group(XingzeCraftDriveMod.XCDM_STATION_GROUP)));
		Registry.register(Registry.BLOCK, new Identifier("xcdm", "station_sign_mc02"), Station_Sign_MC02);
		Registry.register(Registry.ITEM, new Identifier("xcdm", "station_sign_mc02"),
				new BlockItem(Station_Sign_MC02, new Item.Settings().group(XingzeCraftDriveMod.XCDM_STATION_GROUP)));
		Registry.register(Registry.BLOCK, new Identifier("xcdm", "station_sign_mc03"), Station_Sign_MC03);
		Registry.register(Registry.ITEM, new Identifier("xcdm", "station_sign_mc03"),
				new BlockItem(Station_Sign_MC03, new Item.Settings().group(XingzeCraftDriveMod.XCDM_STATION_GROUP)));
		Registry.register(Registry.BLOCK, new Identifier("xcdm", "station_sign_mc04"), Station_Sign_MC04);
		Registry.register(Registry.ITEM, new Identifier("xcdm", "station_sign_mc04"),
				new BlockItem(Station_Sign_MC04, new Item.Settings().group(XingzeCraftDriveMod.XCDM_STATION_GROUP)));
		Registry.register(Registry.BLOCK, new Identifier("xcdm", "station_sign_mc05"), Station_Sign_MC05);
		Registry.register(Registry.ITEM, new Identifier("xcdm", "station_sign_mc05"),
				new BlockItem(Station_Sign_MC05, new Item.Settings().group(XingzeCraftDriveMod.XCDM_STATION_GROUP)));
		Registry.register(Registry.BLOCK, new Identifier("xcdm", "station_sign_mc06"), Station_Sign_MC06);
		Registry.register(Registry.ITEM, new Identifier("xcdm", "station_sign_mc06"),
				new BlockItem(Station_Sign_MC06, new Item.Settings().group(XingzeCraftDriveMod.XCDM_STATION_GROUP)));
		Registry.register(Registry.BLOCK, new Identifier("xcdm", "railway_sign_stop"), railway_sign_stop);
		Registry.register(Registry.ITEM, new Identifier("xcdm", "railway_sign_stop"),
				new BlockItem(railway_sign_stop, new Item.Settings().group(XingzeCraftDriveMod.XCDM_STATION_GROUP)));
		LOGGER.info("XingzeCraftDriveMod is loaded!");
	}

	public static final ItemGroup XCDM_STATION_GROUP = FabricItemGroupBuilder.build(
			new Identifier("xcdm", "station"),
			() -> new ItemStack(Blocks.COBBLESTONE));
}
